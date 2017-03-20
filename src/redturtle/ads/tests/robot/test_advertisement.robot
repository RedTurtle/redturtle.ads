# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s redturtle.ads -t test_advertisement.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src redturtle.ads.testing.REDTURTLE_ADS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_advertisement.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Advertisement
  Given a logged-in site administrator
    and an add advertisement form
   When I type 'My Advertisement' into the title field
    and I submit the form
   Then a advertisement with the title 'My Advertisement' has been created

Scenario: As a site administrator I can view a Advertisement
  Given a logged-in site administrator
    and a advertisement 'My Advertisement'
   When I go to the advertisement view
   Then I can see the advertisement title 'My Advertisement'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add advertisement form
  Go To  ${PLONE_URL}/++add++Advertisement

a advertisement 'My Advertisement'
  Create content  type=Advertisement  id=my-advertisement  title=My Advertisement


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the advertisement view
  Go To  ${PLONE_URL}/my-advertisement
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a advertisement with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the advertisement title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
