from utils import dicts


def test_get():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs") == 'mercurial'
    assert dicts.get_val({}, "vcs") == 'git'
    assert dicts.get_val({}, "vcs", "bazaar") == 'bazaar'




