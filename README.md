
<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/zuri-training/qr_gen_team60/">
    <img src="https://github.com/zuri-training/qr_gen_team60/blob/main/qr_gen_project/static/base/images/qr_logo.png" alt="Logo" width="300" height="250">
  </a>

<h3 align="center">QR Planet</h3>
  <p align="center"><h3>
    </h3>
    <br />
    <h2><a href="https://github.com/zuri-training/qr_gen_team60/qr_gen_project/docs/README.md"><strong>Explore the docs »</strong></a></h2>
    <br />
    <a href="">View Demo</a>
    ·
    <a href="#issues">Report Bug</a>
    ·
    <a href="#issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-documentation">Project Documentation</a></li>
        <li><a href="#project-figma-board">Project Figma Board</a></li>  
        <li><a href="#github-project-organization">Github Project Organization</a></li>  
        <li><a href="#technologies-used">Technologies Used</a></li>
        <li><a href="#features">Features</a></li>
      </ul>
    </li>
    <li>
      <a href="#how-to-use">How to use Locally</a>
      <ul>
        <li><a href="#requirements">Requirements</a></li>
        <li><a href="#how-to-contribute">How to contribute</a></li>
        <li><a href="#setup-and-installation">How to Use</a></li> 
        <li><a href="#contributors">Collaborators</a></li>
      </ul>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## `About The Project:`
QR Planet is a web app that focuses on generating QR  codes that perform tasks involving encoding information. The codes generated can be shared directly via email or any other social media platform while also giving users the option to download the QR codes generated in various formats.


<!-- Project Documentation -->
#### `Project Documentation:`
> <a href="https://docs.google.com/document/d/11YqY3GACwCbnjsB-XrjberOGCVKw7SUvrz6sGoQM0_s/edit">Team 60 QR Generator Docs</a>

<!-- Project Figma Board -->
#### `Project Figma Board:`
> <a href="https://www.figma.com/file/IsSByeqo1V0yS9QW6wmS8j/QR_GENERATOR-PROJECT">Team 60 QR Generator</a>

<!-- Github Project Organization -->
#### `Github Project Organization:`
> <a href="https://github.com/orgs/zuri-training/projects/299">Team 60 Github Projects</a>


## __Project Status__: _in progress_
<br><br>

## `Technologies Used`
  - __Design__ <br/>
  ![figma-#F24E1E](https://user-images.githubusercontent.com/72948572/183909728-8197f9c8-8b97-4015-8e0b-f8e605b19309.svg)
  
  - __Frontend__ <br/>
![html5-#E34F26](https://user-images.githubusercontent.com/72948572/183910382-06b2d259-2f17-4c4f-afb0-0ed20cddd85c.svg) ![css3-#1572B6](https://user-images.githubusercontent.com/72948572/183910424-215b3da2-9067-44ba-a16a-91eefc3d90fc.svg) ![javascript-#323330](https://user-images.githubusercontent.com/72948572/183910461-4e24a5f5-7ad9-48a0-a7b0-94bcba32a94b.svg)

  - __Backend__ <br/>
  ![python-3670A0](https://user-images.githubusercontent.com/72948572/183910681-b6193dcd-8242-4a5e-af78-d79f99fc40b6.svg) ![django-#092E20](https://user-images.githubusercontent.com/72948572/183910701-cdc634b5-9524-4158-8063-045000741e42.svg)

  - __Database__ <br/>
  ![POSTGRE-SQL-brightgreen](https://user-images.githubusercontent.com/72948572/183910301-8bcb404e-4fdd-497f-a493-a33430561a9b.svg)
  
  - __Project Mnagement__ <br/>
  ![github-#121011](https://user-images.githubusercontent.com/72948572/183911700-45ab5ec7-8f95-41ce-8d0e-616ddca2827f.svg)
  <br><br>

## `Features`
  `Create Account` Users are able to sign up on *`QR Planet`* with their email, username,  and password. 
  
  `Login` Fetches users sign up details from our database, compares the login details and allows authenticated users gain full access to `QR Planet's` Services.
  
  `Documentation` All Users have full access to view the documentation, only Authenticated Users Can interact with it.

  `Generate QR Codes` Authenticated users can Generate Qr for Different use case, Email, Text, Url App-store, etc.
  
  `Download QR Codes` Authenticated users Can download a generated QR code into their Local Device as PDF, PNG, JPEG, JPG or Even SVG

  `Save QR codes` Authenticated users Can save a Generated QR code to view Later

  `Share` Authenticated users can share Generated QR codes to Twitter, Facebook or Even as an Email.

  
  `Responsive` Enables users to access the platform via their various devices without any issues with their display.

  <br><br>

  ## `How To Use Locally:`
<br>


## `Requirements`
* An IDE
* Git & GitHub 
* A compatible browser
* Python 3.8+
  <br><br>


##  `Setup and Installation`  
  __In your IDE run the following commands in the terminal to setup__
- Install  environment in the root directory `qr_gen_project`

    ``` ruby
    pip install virtualenv
    ```
- Create the virtual environment in the same root directory

  - FOR WINDOWS USERS

    ``` ruby
    virtualenv <environment_name>
    ``` 
    - Activate virtual environment

      ``` ruby
      <environment_name>\scripts\activate
      ``` 

  - FOR LINUX USERS

    ``` ruby
    python3 -m virtualenv <environment_name>
    ``` 
    - Activate virtual environment

      ``` ruby
      source/<environment_name>/bin/activate
      ```
  <br>

- Change directory

  ``` ruby
  cd qr_gen_team60/qr_gen_project/
  ```
<br>


- Install all packages/ Dependencies used
    ``` ruby
    pip install -r requirements.txt
    ```
- Run Migrations for the Apps

    ``` ruby
    python manage.py makemigrations accounts
    ``` 

  
    ``` ruby
    python manage.py makemigrations qr_generator
    ```


    ``` ruby
    python manage.py migrate accounts
    ```

    ``` ruby
    python manage.py migrate qr_generator
    ``` 

  ``` ruby
    python manage.py migrate
    ```

- Run Server

    ``` ruby
    python manage.py runserver
    ```

  <br><br>
## `How to Contribute `
- __Fork the project repository__<br/>
In the project repository on github click the fork button in the upper right corner

- __Clone the forked repository to your local machine__

    ```ruby
    git clone https://github.com/zuri-training/qr_gen_team60.git
    ```
- __Navigate to the local directory and open in your IDE/ Text Editor__

- __In the IDE terminal set upstream branch__

    ```ruby
    git remote add upstream https://github.com/zuri-training/qr_gen_team60.git
    ```
- __Pull upstream__

    ```ruby
    git pull upstream production
    ```
    
- __Create a new branch to make your changes__

    ```ruby
    git checkout -b <your_branch_name>
    ```
    
- __Stage the file__
After making edits, type the below command in your terminal

    ```ruby
    git add <changed_files>
    ```
    
- __Commit changes__

    ```ruby
    git commit -m "your_message"
    ```
- __Push your local changes__

    ```ruby
    git push origin <your_branch_name>
    ```

- __Create a pull request__

- __Wait till a QR planet admin accepts and merges your pull request__

  <br><br>

## `Contributors`

|__Name__ | __Slack Username__| __Track__|
|:--------|:------------------|-----------:|
| [Elizabeth Ogunmola](https://github.com/)| `Elizzy`|`Fullstack-Developer`|
| [Temitope Yusuff](https://github.com/)| `Temitope_OX`|`Fullstack-Developer`|
| [Oluwabemisoke Aseperi](https://github.com/)| `Gbemisoke`|`Product Designer`|
| [Wisdom Emmanuel](https://github.com/SimpleNiQue)| `SimpleNick`|`Fullstack-Developer`|
| [Kingsley Onoriode](https://github.com/)| `Ononero`|`Product Designer`|
| [Odekunle Joseph](https://github.com/)| `---`|`Product Designer`|
| [Ibrahim Tomiwa](https://github.com/)| `Ire'Oluwatomiwa`|`Product Designer`|
| [Joshua Oladoye-Sule](https://github.com/)| `--`|`Product Designer`|
| [Ifeoma Sylvia Dike](https://github.com/)| `Ifeoma Sylvia Dike`|`Product Designer`|
| [Saminu Mojisola](https://github.com/)| `---`|`Product Designer`|
| [Raji John Damisa](https://github.com/)| `---`|`Product Designer`|
| [Ndafohamba Shadjanale](https://github.com/)| `NdafohambaS`|`Product Designer`|
  <br>  <br><br>
<div align="center">
    <h1 >What are You Waiting For?? Try out QR Planet Today!!!</h1>
</div>

![QR Planet](https://github.com/zuri-training/qr_gen_team60/blob/main/qr_gen_project/static/base/gif/qr.gif)

<p align="right">(<a href="#top">back to top</a>)</p>
