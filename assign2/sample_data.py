from solution import FileNode


def makeData(which):
    if which == 1:
        '''
        root
            one
            another
                whee
        '''
        nodes1 = {}
        root1 = nodes1["root"] = FileNode("root", data=None)
        nodes1["one"] = FileNode("one", parent=nodes1["root"], data=None)
        nodes1["another"] = FileNode("another", parent=nodes1["root"], data=None)
        nodes1["whee"] = FileNode("whee", parent=nodes1["another"], data=None)
        return root1, nodes1

    if which == 2:
        '''
        alpha
            beta
                gamma
                delta
                    epsilon
            foo
            bar
            baz
                glurp
                blort
        '''
        nodes2 = {}
        root2 = nodes2['alpha'] = FileNode('alpha', data=None)
        nodes2['beta'] = FileNode('beta', parent=nodes2['alpha'], data=None)
        nodes2['foo'] = FileNode('foo', parent=nodes2['alpha'], data=None)
        nodes2['bar'] = FileNode('bar', parent=nodes2['alpha'], data=None)
        nodes2['baz'] = FileNode('baz', parent=nodes2['alpha'], data=None)
        nodes2['gamma'] = FileNode('gamma', parent=nodes2['beta'], data=None)
        nodes2['delta'] = FileNode('delta', parent=nodes2['beta'], data=None)
        nodes2['glurp'] = FileNode('glurp', parent=nodes2['baz'], data=None)
        nodes2['blort'] = FileNode('blort', parent=nodes2['baz'], data=None)
        nodes2['epsilon'] = FileNode('epsilon', parent=nodes2['delta'], data=None)
        return root2, nodes2

    if which == 3:
        '''
        figure it out
        '''
        nodes3 = {}
        root3 = nodes3["/"] = FileNode("/", data=None)
        nodes3["etc"] = FileNode("etc", parent=nodes3["/"], data=None)
        nodes3["home"] = FileNode("home", parent=nodes3["/"], data=None)
        nodes3["vim"] = FileNode("vim", parent=nodes3["etc"], data=None)
        nodes3["postgres"] = FileNode("postgres", parent=nodes3["etc"], data=None)
        nodes3["jholman"] = FileNode("jholman", parent=nodes3["home"], data=None)
        nodes3["tholane"] = FileNode("tholane", parent=nodes3["home"], data=None)
        nodes3["smeechward"] = FileNode("smeechward", parent=nodes3["home"], data=None)
        nodes3["vimrc"] = FileNode("vimrc", parent=nodes3["vim"], data=None)
        nodes3["vimrc.tiny"] = FileNode("vimrc.tiny", parent=nodes3["vim"], data=None)
        nodes3["12"] = FileNode("12", parent=nodes3["postgres"], data=None)
        nodes3[".bashrc"] = FileNode(".bashrc", parent=nodes3["jholman"], data=None)
        nodes3[".vimrc1"] = FileNode(".vimrc", parent=nodes3["jholman"], data=None)
        nodes3["algorithms"] = FileNode(
            "algorithms", parent=nodes3["jholman"], data=None
        )
        nodes3["fswd"] = FileNode("fswd", parent=nodes3["jholman"], data=None)
        nodes3["zybooks"] = FileNode("zybooks", parent=nodes3["tholane"], data=None)
        nodes3[".bashrc"] = FileNode(".bashrc", parent=nodes3["tholane"], data=None)
        nodes3[".vimrc2"] = FileNode(".vimrc", parent=nodes3["tholane"], data=None)
        nodes3["grading"] = FileNode("grading", parent=nodes3["tholane"], data=None)
        nodes3[".bashrc"] = FileNode(".bashrc", parent=nodes3["smeechward"], data=None)
        nodes3[".vimrc3"] = FileNode(".vimrc", parent=nodes3["smeechward"], data=None)
        nodes3["stupid_scooter_project"] = FileNode(
            "stupid_scooter_project", parent=nodes3["smeechward"], data=None
        )
        nodes3["stupid_advent_project"] = FileNode(
            "stupid_advent_project", parent=nodes3["smeechward"], data=None
        )
        nodes3["youtube"] = FileNode("youtube", parent=nodes3["smeechward"], data=None)
        nodes3["main"] = FileNode("main", parent=nodes3["12"], data=None)
        nodes3["cruelty.md"] = FileNode(
            "cruelty.md", parent=nodes3["algorithms"], data=None
        )
        nodes3["hilarious_misery.md"] = FileNode(
            "hilarious_misery.md", parent=nodes3["algorithms"], data=None
        )
        nodes3["pain.md"] = FileNode("pain.md", parent=nodes3["algorithms"], data=None)
        nodes3["suffering.md"] = FileNode(
            "suffering.md", parent=nodes3["algorithms"], data=None
        )
        nodes3["arbeit_macht_frei.md"] = FileNode(
            "arbeit_macht_frei.md", parent=nodes3["fswd"], data=None
        )
        nodes3["wk1.ipy"] = FileNode("wk1.ipy", parent=nodes3["zybooks"], data=None)
        nodes3["wk2.ipy"] = FileNode("wk2.ipy", parent=nodes3["zybooks"], data=None)
        nodes3["wk3.ipy"] = FileNode("wk3.ipy", parent=nodes3["zybooks"], data=None)
        nodes3["auto_test_harness.py"] = FileNode(
            "auto_test_harness.py", parent=nodes3["grading"], data=None
        )
        nodes3["why_do_they_do_this.py"] = FileNode(
            "why_do_they_do_this.py", parent=nodes3["grading"], data=None
        )
        nodes3["batteries.md"] = FileNode(
            "batteries.md", parent=nodes3["stupid_scooter_project"], data=None
        )
        nodes3["wiring.md"] = FileNode(
            "wiring.md", parent=nodes3["stupid_scooter_project"], data=None
        )
        nodes3["razorblades.md"] = FileNode(
            "razorblades.md", parent=nodes3["stupid_advent_project"], data=None
        )
        nodes3["servos.md"] = FileNode(
            "servos.md", parent=nodes3["stupid_advent_project"], data=None
        )
        nodes3["latest_video.mp4"] = FileNode(
            "latest_video.mp4", parent=nodes3["youtube"], data=None
        )
        nodes3["profile.jpg"] = FileNode(
            "profile.jpg", parent=nodes3["youtube"], data=None
        )
        nodes3["pg_hba.conf"] = FileNode(
            "pg_hba.conf", parent=nodes3["main"], data=None
        )
        return root3, nodes3
