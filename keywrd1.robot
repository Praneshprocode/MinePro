*** Settings ***
Library         SeleniumLibrary


*** Keywords ***
Value_Enter
    [Arguments]              ${name}     ${password}
    Open Browser        ${url}      ${browser}
    Input Text         xpath=//input[@name="userid"]       ${name}
    Input Text        xpath=//input[@name="pswrd"]        ${password}
    ${titleget}         get title
    [Return]            ${titleget}
EndBrowser
        Close Browser

