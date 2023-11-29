*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${APP_URL}             http://localhost:8090/
${APP_TITLE}           Lotto App
${BROWSER}             firefox


*** Keywords ***
Open Browser to Main Page
    [Documentation]    Open browser to Application main page.
    ${is_os_linux}=    Evaluate    sys.platform=="linux"    modules=sys
    IF    $is_os_linux
        Open Browser    ${APP_URL}    edge
    ELSE
        Open Browser    ${APP_URL}    ${BROWSER}
    END


*** Test Cases ***
Application Appears as Expected on Startup
    [Tags]    test_set_1
    Open Browser to Main Page
    Validate App Title
    Close Browser

