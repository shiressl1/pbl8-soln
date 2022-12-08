def test_new_user_not_logged_in(general_public_user):
    """
    GIVEN a new user (created as a fixture)
    WHEN the user has just been created
    THEN the logged in status should be False
    """
    assert general_public_user.is_logged_in is True
