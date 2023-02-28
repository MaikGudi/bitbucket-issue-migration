# Mercurial user to be used for the commits of the migration
#MIGRATION_COMMITS_USER = "Viper Admin <viper-admin@inf.ethz.ch>"


# Github only accepts assignees from valid users. We map those users from bitbucket.


USER_MAPPING = {
    "maik.gudi": "MaikGudi",
    "{62beb341d752af0e54edcd11}": "MaikGudi"
}

# We map bitbucket's issue "kind" to github "labels".
KIND_MAPPING = {
    "bug": "bug",
    "enhancement": "enhancement",
    "proposal": "proposal",
    "task": "task",
}

# We map bitbucket's issue "priority" to github "labels".
PRIORITY_MAPPING = {
    "trivial": "trivial",
    "minor": "minor",
    "major": "major",
    "critical": "critical",
    "blocker": "blocker",
}

# We map bitbucket's issue "component" to github "labels".
COMPONENT_MAPPING = {
    "Consistency": "consistency",
    "Parser": "parser",
    "silver-obligations": "silver-obligations",
    "Triggers": "triggers",
    "Examples": "examples",
    "Functions": "functions",
    "Logging, Reporting, IDE": "logging-reporting-ide",
    "Magic Wands": "magic-wands",
    "Permissions": "permissions",
    "Quantified Permissions": "quantified-permissions",
    "Silver": "silver",
    "Z3": "z3"
}

# The only github states are "open" and "closed".
# Therefore, we map some bitbucket states to github "labels".
STATE_MAPPING = {
    "on hold": "on hold",
    "invalid": "invalid",
    "duplicate": "duplicate",
    "wontfix": "wontfix",
    "resolved": None,
    "new": None,
    "open": None,
    "closed": None,
    "DECLINED": "declined",
    "MERGED": "merged",
    "SUPERSEDED": "superseeded",
    "OPEN": None,
}

# Bitbucket has several issue and pull request states.
# All states that are not listed in this set will be closed.
OPEN_ISSUE_OR_PULL_REQUEST_STATES = {
    "open",
    "new",
    "on hold",
    "OPEN",
}

# Mapping of known Bitbucket to their corresponding GitHub repo
# This information is used to convert links
KNOWN_REPO_MAPPING = {
    "maikgudi/testissuemigration": "MaikGudi/TestPullRequestMigration2"
}

# Mapping of known Bitbucket repos to their number of issues.
# This information is used to correctly account for the offset
# of PRs' IDs
KNOWN_ISSUES_COUNT_MAPPING = {
    "maikgudi/testissuemigration": 0
}

KNOWN_CMAP_PATHS = {
    "maikgudi/testissuemigration": "migration_data/cmap.txt"
}
