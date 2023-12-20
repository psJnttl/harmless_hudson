*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${APP_URL}             http://localhost:8090/
${APP_TITLE}           Lotto App
${BROWSER}             firefox
${APP_PAGE_HEADING}    Select Lotto Flavour
${LOTTERY1_TITLE}      Veikkaus Lotto
${LOTTERY1_LINK}       Veikkaus
${LOTTERY1_HEADING}    New numbers for Veikkaus Lotto
${LOTTERY2_LINK}       Viking
${LOTTERY2_HEADING}    New numbers for Viking Lotto
${LOTTERY2_TITLE}      Viking Lotto
${LOTTERY3_LINK}       Euro Jackpot
${LOTTERY3_HEADING}    New numbers for Euro Jackpot Lotto
${LOTTERY3_TITLE}      Euro Jackpot Lotto

*** Keywords ***
Open Headless Edge Browser to URL
    [Documentation]    Open Browser to URL in headless mode.
    [Arguments]    ${URL}
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()
    Call Method    ${options}    add_argument    --headless
    Create Webdriver    Edge    options=${options}
    Go To    ${URL}

Open Browser to Main Page
    [Documentation]    Open browser to Application main page.
    ${is_os_linux}=    Evaluate    sys.platform=="linux"    modules=sys
    IF    $is_os_linux
        Open Headless Edge Browser to URL    ${APP_URL}
    ELSE
        Open Browser    ${APP_URL}    ${BROWSER}
    END

Validate App Title
    [Documentation]    Make sure that the title of the App page is correct.
    Title Should Be    ${APP_TITLE}

Validate Page Heading
    [Documentation]    Checks that the heading on Main page is correct.
    Page Should Contain Element    xpath=/html/body/h4[text()="${APP_PAGE_HEADING}"]

Can Display Selected Lotto Flavour Numbers
    [Arguments]    ${LOTTERY_LINK}    ${LOTTERY_HEADING}    ${LOTTERY_TITLE}    ${NUMBER_IN_LIST}
    Page Should Contain Link    xpath=/html/body/table/tbody/tr[${NUMBER_IN_LIST}]/td[1]/a[text()="${LOTTERY_LINK}"]
    Click Link    xpath=/html/body/table/tbody/tr[${NUMBER_IN_LIST}]/td[1]/a[text()="${LOTTERY_LINK}"]
    Wait Until Page Contains Element    timeout=1s
    ...    locator=xpath=/html/body/h5[text()="${LOTTERY_HEADING}"]
    Title Should Be    ${LOTTERY_TITLE}
    Wait Until Page Contains Element    timeout=1s
    ...    locator=xpath=/html/body/span[@class="lotto-numbers"]


*** Test Cases ***
Application Appears as Expected on Startup
    [Tags]    test_set_1
    Open Browser to Main Page
    Validate App Title
    Validate Page Heading
    Close Browser

Can Display Veikkaus Lotto Numbers
    [Tags]    test_set_1
    Open Browser to Main Page
    Can Display Selected Lotto Flavour Numbers    ${LOTTERY1_LINK}    ${LOTTERY1_HEADING}    ${LOTTERY1_TITLE}    1
    Close Browser

Can Display Viking Lotto Numbers
    [Tags]    test_set_1
    Open Browser to Main Page
    Can Display Selected Lotto Flavour Numbers    ${LOTTERY2_LINK}    ${LOTTERY2_HEADING}    ${LOTTERY2_TITLE}    2
    Close Browser

Can Display Euro Jackpot Lotto Numbers
    [Tags]    test_set_1
    Open Browser to Main Page
    Can Display Selected Lotto Flavour Numbers    ${LOTTERY3_LINK}    ${LOTTERY3_HEADING}    ${LOTTERY3_TITLE}    3
    Close Browser
