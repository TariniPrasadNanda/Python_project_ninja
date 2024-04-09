*** Settings ***


Library      SeleniumLibrary
Resource    ${CURDIR}/Resources/resources.robot


*** Variable ***

${URL}                https://www.saucedemo.com/v1/
${BROWSER}            chrome
${STANDARD_USER}      standard_user
${LOCKED_USER}        locked_out_user
${PROBLEM_USER}       problem_user
${GLITCH_USER}        performance_glitch_user
${PASSWORD_ALL}       secret_sauce
${username_field}     //input[@id='user-name']
${password_field}     //input[@id='password']
${logIn_Button}       //input[@id='login-button']

*** Test Cases ***
login with standard user
    Launch browser with URL   ${URL}  ${BROWSER}
    sleep   2s
    maximize browser window
    set input on text box   ${username_field}   ${STANDARD_USER}
    sleep   2s
    set input on text box   ${password_field}   ${PASSWORD_ALL}
    sleep   2s
    push button             ${logIn_Button}
    sleep   5s
    close Browser


login with locked_out user
    Launch browser with URL   ${URL}  ${BROWSER}
    sleep   2s
    maximize browser window
    set input on text box   ${username_field}   ${LOCKED_USER}
    sleep   2s
    set input on text box   ${password_field}   ${PASSWORD_ALL}
    sleep   2s
    push button             ${logIn_Button}
    sleep   5s
    close Browser

login with problem user
    Launch browser with URL   ${URL}  ${BROWSER}
    sleep   2s
    maximize browser window
    set input on text box   ${username_field}   ${PROBLEM_USER}
    sleep   2s
    set input on text box   ${password_field}   ${PASSWORD_ALL}
    sleep   2s
    push button             ${logIn_Button}
    sleep   5s
    close Browser

login with performance_glitch user
    Launch browser with URL   ${URL}  ${BROWSER}
    sleep   2s
    maximize browser window
    set input on text box   ${username_field}   ${GLITCH_USER}
    sleep   2s
    set input on text box   ${password_field}   ${PASSWORD_ALL}
    sleep   2s
    push button             ${logIn_Button}
    sleep   5s
    close Browser



