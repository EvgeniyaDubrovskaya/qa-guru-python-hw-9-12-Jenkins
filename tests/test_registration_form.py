from selene import command, have, browser


def test_register_user_success():
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        have.size_greater_than_or_equal(3))
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    browser.element('#firstName').type('Jane')
    browser.element('#lastName').type('Doe')





