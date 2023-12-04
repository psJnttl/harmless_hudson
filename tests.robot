*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${APP_URL}             http://localhost:8090/
${APP_TITLE}           Lotto App
${BROWSER}             firefox
${APP_PAGE_HEADING}    Select Lotto Flavour
${LOTTERY1_TITLE}      Veikkaus Lotto
${LOTTERY1_LINK}       Veikkaus Lotto
${LOTTERY1_HEADING}    New numbers for Veikkaus Lotto
${LOTTERY2_LINK}       Viking Lotto
${LOTTERY2_HEADING}    New numbers for Viking Lotto
${LOTTERY2_TITLE}      Viking Lotto
${LOTTERY3_LINK}       Euro Jackpot Lotto
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
    Page Should Contain Link    xpath=//html/body/a[text()="${LOTTERY1_LINK}"]
    Click Link    xpath=/html/body/a[text()="${LOTTERY1_LINK}"]
    Wait Until Page Contains Element    timeout=1s
    ...    locator=xpath=/html/body/h5[text()="${LOTTERY1_HEADING}"]
    Title Should Be    ${LOTTERY1_TITLE}
    Wait Until Page Contains Element    timeout=1s
    ...    locator=xpath=/html/body/span[@class="lotto-numbers"]
    Close Browser

Can Display Viking Lotto Numbers
    [Tags]    test_set_1
    Open Browser to Main Page
    Page Should Contain Link    xpath=//html/body/a[text()="${LOTTERY2_LINK}"]
    Click Link    xpath=/html/body/a[text()="${LOTTERY2_LINK}"]
    Wait Until Page Contains Element    timeout=1s
    ...    locator=xpath=/html/body/h5[text()="${LOTTERY2_HEADING}"]
    Title Should Be    ${LOTTERY2_TITLE}
    Wait Until Page Contains Element    timeout=1s
    ...    locator=xpath=/html/body/span[@class="lotto-numbers"]
    Close Browser

Can Display Euro Jackpot Lotto Numbers
    [Tags]    test_set_1
    Open Browser to Main Page
    Page Should Contain Link    xpath=//html/body/a[text()="${LOTTERY3_LINK}"]
    Click Link    xpath=/html/body/a[text()="${LOTTERY3_LINK}"]
    Wait Until Page Contains Element    timeout=1s
    ...    locator=xpath=/html/body/h5[text()="${LOTTERY3_HEADING}"]
    Title Should Be    ${LOTTERY3_TITLE}
    Wait Until Page Contains Element    timeout=1s
    ...    locator=xpath=/html/body/span[@class="lotto-numbers"]
    Close Browser
