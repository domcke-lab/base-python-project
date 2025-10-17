def test_placeholder() -> None:
    """Basic sanity check to verify the test harness is wired up."""
    assert True

def test_environment_setup():
    from myPackage import myAnalysisTools

def test_add_one():
    from myPackage import myAnalysisTools

    x = 2
    y = myAnalysisTools.add_one(x)

    assert y == x + 1
