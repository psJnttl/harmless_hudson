*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${APP_URL}             http://localhost:8090/
${APP_TITLE}           Lotto App
${BROWSER}             firefox
${APP_PAGE_HEADING}    Select Lotto Flavour

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
