#!/usr/bin/env python

# Path to rbt script
POSTREVIEW_PATH = "/usr/local/bin/"

# Username and password for Review Board
USERNAME = 'ericsson'
PASSWORD = 'ericsson'

# If true, runs rbt in debug mode and outputs its diff
DEBUG = True

import sys
import os
import subprocess
import re
import svn.fs
import svn.core
import svn.repos

# list of trac commands from trac-post-commit-hook.py.
# numbers following these commands will be added to the bugs
# field of the review request.
supported_ticket_cmds = {'review':         '_cmdReview',
                         'publishreview':  '_cmdReview',
                         'publish review': '_cmdReview',
                         'draftreview':    '_cmdReview',
                         'draft review':   '_cmdReview'}

ticket_prefix = '(?:#|(?:ticket|issue|bug)[: ]?)'
ticket_reference = ticket_prefix + '[0-9]+'
ticket_command = (r'(?P<action>[A-Za-z]*).?'
                  '(?P<ticket>%s(?:(?:[, &]*|[ ]?and[ ]?)%s)*)' %
                  (ticket_reference, ticket_reference))

def execute(command, env=None, ignore_errors=False):
    """
    Utility function to execute a command and return the output.
    Derived from Review Board's rbt script.
    """
    if env:
        env.update(os.environ)
    else:
        env = os.environ

    p = subprocess.Popen(command,
                         stdin = subprocess.PIPE,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.STDOUT,
                         shell = False,
                         close_fds = sys.platform.startswith('win'),
                         universal_newlines = True,
                         env = env)

    data = p.stdout.read()

    rc = p.wait()
    if rc and not ignore_errors:
        sys.stderr.write('Failed to execute command: %s\n%s\n' % (command, data))
        sys.exit(1)

    return data

def main():
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: %s <repos> <rev>\n' % sys.argv[0])
        sys.exit(1)

    repos = sys.argv[1]
    rev = sys.argv[2]

    # verify that rev parameter is an int
    try:
        int(rev)
    except ValueError:
        sys.stderr.write("Parameter <rev> must be an int, was given %s\n" % rev)
        sys.exit(1)

    # get the svn file system object
    fs_ptr = svn.repos.svn_repos_fs(svn.repos.svn_repos_open(
            svn.core.svn_path_canonicalize(repos)))

    # get the log message
    log = svn.fs.svn_fs_revision_prop(fs_ptr, int(rev),
                                    svn.core.SVN_PROP_REVISION_LOG)

    # error if log message is blank
    if len(log.strip()) < 1:
        sys.stderr.write("Log message is empty, no review request created\n")
        sys.exit(1)

    # get the author
    author = svn.fs.svn_fs_revision_prop(fs_ptr, int(rev),
                                       svn.core.SVN_PROP_REVISION_AUTHOR)

    if not author:
       author = "ericsson"    

    # check whether to create a review, based on presence of word
    # 'review' with prefix
    review = r'(?:publish|draft)(?: )?review'

    if not re.search(review, log, re.M | re.I):
        print 'No review requested'
        sys.exit(0)

    # check for update to existing review
    m = re.search(r'update(?: )?review:([0-9]+)', log, re.M | re.I)
    if m:
        reviewid = '--review-request-id=' + m.group(1)
    else:
        reviewid = ''

    # check whether to publish or leave review as draft
    if re.search(r'draft(?: )?review', log, re.M | re.I):
        publish = ''
    else:
        publish = '-p'

    # get previous revision number -- either 1 prior, or
    # user-specified number
    m = re.search(r'after(?: )?revision:([0-9]+)', log, re.M | re.I)
    if m:
        prevrev = m.group(1)
    else:
        prevrev = int(rev) - 1

    # check for an explicitly-provided base path (must be contained
    # within quotes)
    m = re.search(r'base ?path:[\'"]([^\'"]+)[\'"]', log, re.M | re.I)
    if m:
        base_path = m.group(1)
    else:
        base_path = ''

    # get bug numbers referenced in this log message
    ticket_command_re = re.compile(ticket_command)
    ticket_re = re.compile(ticket_prefix + '([0-9]+)')

    ticket_ids = []
    ticket_cmd_groups = ticket_command_re.findall(log)
    for cmd, tkts in ticket_cmd_groups:
        funcname = supported_ticket_cmds.get(cmd.lower(), '')
        if funcname:
            for tkt_id in ticket_re.findall(tkts):
                ticket_ids.append(tkt_id)

    if ticket_ids:
        bugs = '--bugs-closed=' + ','.join(ticket_ids)
    else:
        bugs = ''

    # summary is log up to first period+space / first new line / first 250 chars
    # (whichever comes first)
    summary = '--summary=' + log[:250].splitlines().pop(0).split('. ').pop(0)

    # other parameters for postreview
    repository_url  = '--repository-url=file://' + repos
    password        = '--password=' + PASSWORD
    username        = '--username=' + USERNAME
    description     = "--description=(In [%s]) %s" % (rev, log)
    submitas        = '--submit-as=' + author
    revision        = '%s %s' % (prevrev, rev)

    # common arguments
    args = [repository_url, username, password, publish,
            submitas, base_path, reviewid]

    # filter out any potentially blank args, which will confuse rbt
    args = [i for i in args if len(i) > 1]

    # if not updating an existing review, add extra arguments
    if len(reviewid) == 0:
        args += [summary, description, bugs]

    args += [revision]

    if DEBUG:
        args += ['-d']
        print [os.path.join(POSTREVIEW_PATH, 'rbt'), 'post'] + args

    # Run Review Board rbt script
    data = execute([os.path.join(POSTREVIEW_PATH, 'rbt'), 'post'] + args,
                   env = {'LANG': 'en_US.UTF-8'})

    if DEBUG:
        print data

if __name__ == '__main__':
    main()
