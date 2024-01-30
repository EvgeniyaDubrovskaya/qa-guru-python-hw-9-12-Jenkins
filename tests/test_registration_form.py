import allure
from selene import command, have, browser

from helpers import resources


def test_register_user_success():
    with allure.step('Open registrations form'):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
    with allure.step('Fill in form'):
        browser.element('#firstName').type('Jane')
        browser.element('#lastName').type('Doe')
        browser.element('#userEmail').type('some@mail.su')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text('1991')).click()
        browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text('January')).click()
        browser.element(f'.react-datepicker__day--0{10}').click()
        browser.all('[for^=gender-radio]').element_by(have.exact_text('Female')).click()
        browser.element('#userNumber').type('1234567890')
        browser.element('#subjectsInput').click().type('Maths').press_enter()
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Reading')).click()
        browser.element('#currentAddress').type('Some address')
        browser.element('.form-file-label').perform(command.js.scroll_into_view)
        browser.element('#uploadPicture').send_keys(resources.path('windy_hill.jpg'))
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.element('#state').all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
        browser.element('#city').click()
        browser.element('#city').all('[id^=react-select][id*=option]').element_by(have.exact_text('Delhi')).click()

    with allure.step('Submit form'):
        browser.element('#submit').press_enter()

    with allure.step('Check registered user data'):
        browser.element('.table').all('td').even.should(have.exact_texts(
            'Jane Doe',
            'some@mail.su',
            'Female',
            '1234567890',
            '10 January,1991',
            'Maths',
            'Reading',
            'windy_hill.jpg',
            'Some address',
            'NCR Delhi'
        ))
