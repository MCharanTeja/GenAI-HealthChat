# GenAI-HealthChat

# How to run?

### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n medichat python=3.10 -y
```

```bash
conda activate medichat
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up localhost:
```

### Techstack Used:

- Python
- LangChain
- Flask
- GPT
- Pinecone

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

    #with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws


    #Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image

    - Save the URI: 970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

# 6. Configure EC2 as self-hosted runner:

    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO
- PINECONE_API_KEY
- OPENAI_API_KEY

# In Detail Steps to deploy this Gen AI application in AWS Cloud: Continuous Integration & Continuous Delivery/Deployment.(CI/CD) (https://www.youtube.com/watch?v=79TVSqA4wNs)

Overview: We will push the code from our local machine to github. Github will automatically trigger the action to deploy the code to AWS cloud and the endpoint is updated without distrubing the current execution of the application.

Github will automatically trigger the action to deploy the code to AWS cloud with the help of
CI/CD Automation tools such as Github Actions, Jenkins, Circle CI etc.

Deployment Services:
Docker: It is a contenarization service to containerize our code which creates a docker image.
This image can be kept in docker hub or ECR (Elastic Container Registry) from where we can pull and executre this image. If we use Docker, we won't get any setup issues.

ECR: Elastic Container Registy is a AWS service that can store any kind of Docker image which would be private.

EC2: It is Virtual Machine AWS service that offers CPU,GPU based virtual machines with configurations to buy.

Github Action: For CI/CD Management.

Step-1:
Prepare Docker file in your local that contanerizes the entire application. Create Docker ignore file to mention files that are not required for containerization. Next we create a .github folder inside which a workflows folder is create that has a cicd.yaml file that helps to do the ci/cd deployment by using github actions and it also has all the environment variables.
This cicd.yaml file will:
1- Perform continuous integration.
2- It will authenticate with my AWS account.
3- Login with the ECR
4- Whatever Docker image you'll be building will be pushed to the ECR.
5- Then, your continuous deployment will start.
6- Again, it will authenticate wih AWS account and pull the image from ECR to EC2 machine and will execute here.

Step-2:
We login into AWS account and search IAM in searchbar to create IAM user. In the left-hand dashboard, click on users link to see the list of users page. Click on create user which gives a user details popup. Give any username and click on Next. Now select the radio-button "atttach policies directly". Search for the below two policies and select them and click on next and then click on create user. Then, we'll be able to see that our user has been created.
1-AmazonEC2ContainerRegistryFullAccess
2- AmazonEC2FullAccess

Step-3:
Click on that user that was created just now and click on security credentials and scroll down to access keys section and click on create access key which gives access key best practices & alternatives page. Now, select the usecase radio button named as command line Interface(CLI) and select the confirmation check box and click on next. This gives a self-description tag page where you just need to click on "create access key" button.
On clicking it, Retrieve access key page will be shown where we need to click on "download .csv file" button which download a csv file that shouldn't be shared with anyone.

Step-4:
In the seach bar of aws, type ECR and click on the Elastic Contain Registry. On the top right corner, check your appropriate region and note it down as we need it in the ongoing steps. Now, in the landing page of ECR, click on create button under Create a repository. Give any name in the repostiory name text box under general settings. Click on Next which creates our repository which is listed under Private repositories heading. Now, copy the URI of your repo and note it down as we need it in the ongoing steps.

Step-5:
In the seach bar of aws, type EC2 and click on EC2. Click on launch an instance on the landing page. Give and name in the textbox. Under Quick start, select ubuntu machine option. Under Instance type dropdown, atleast 8GB RAM shoud be selected, so we select t2.large. Then, click on Create new key pair Under Key pair (login) and give any keypair name in the create key pair popup and click on create key pair button. This will create a RSF file. A "pem" file will be downloaded which can be used if we use any 3rd party tool such as Putty to connect with your EC2 instance. Now, under Network settings, apart from Allow SSH, also check Allow HTTPS and Allow HTTP. Under Configure Storage, put atleast "30GB" and then click on launch instance button at the bottom right corner. Now, when you click on View all instances button on the landing page, this would give us an instances page, where we could see our machine running. Click on that instance id link of our machine and click on connect button on the top right corner of the landing page. This would open a Connect to instance page where you could see "Connect using EC2 instance connect" is pre-selected, so you just click on connect button on the button right of the same page. This would create a new block terminal in a new tab that we need to use to set up everything which is our production server where we don't see any UI and we have to communicate using the linux terminal that shows up.

Step-6:
We need to update the machine, so we give the exeute the below commands in order one afer another:
sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker

Now, we run "docker --version" to check the version which means the docker is installed successfully. Now, we have to configure our EC2 as a self-hosted runner that means we have to connect our github so that whever the developer pushes the code in github, it will automatically be updated in aws cloud. Go to our repository in github and on this page, click on settings. Click on Action and click on runners on the left menu of the landing page. Click on "New Self-hosted Runner" green button on the Runners landing page. On the next landing page, select the linux option under Runner image. Now, copy each of the commands under Download section, followed by configure section and execute it in the production terminal. Now, Before executing the last command under Configure, in the terminal, it will ask for "Enter the name of the runner group to add this runner to" - just press Enter.
Next it will ask for "Enter the name of the runner". Here, you type: self-hosted and click on enter. Press enter for the additional labels and for the work folder name questions. Now copy the last command "./run.sh" under configure section and execute it in the terminal and it would be connected to the github and shows "Listening for jobs". You can ignore the command "Using your self-hosted runner". Now, if you go back to the Runners option in github, you see the status color as green which means github is connected to our aws cloud.

Step-7:
Setup All the github secrets. Now, under Security section on the left menu on github, click on actions under secrets and variables. Under Repository secrets of the landing page, click on the gree button called "New Repository Secret". Now in the new page called Action Secrets, give the name as "AWS_ACCESS_KEY_ID" and copy the "Access key Id" value present in the accesskey csv file that was downloaded earlier and pase it in the Secret section.Click on "Add Secret button. In the next page, you need to click on new repository secret button under Environent secrets. In the next page, you need to give the name as "AWS_SECRET_ACCESS_KEY" and secret with the value of secret access key present in the accesskey csv file and click on Add secret button. Similary, click on new repository secret button and give the name as "AWS_DEFAULT_REGION" and secret as the region code that we have noted aside previously and click on Add secret button. Next give the name as "ECR_REPO" and secret as the name in the uri (after .com/). Then in the next repository secret give "PINECONE_API_KEY" with its value as secret and another repository secret with name as "OPENAI_API_KEY" and its value as secret.

Step-8:
We push these new git option additions to github by giving a commit message. Now, after pushing these changes, if you refresh the your github repository page, and click on actions tab, you will notice that the action is running. The jobs CI and CD will run automatically. Now, If you open the ECR page and click on images option under private repository on the left side menu and refresh the page, you would notice that the docker image has been uplodaed here. Now, we need to do the port mapping. For this, go to the EC2 instances page and click on instances under instances on the left side menu. Then, click on our instance id link shown in the landing page. Click on security on the landing page. Click on the link below security groups. Now, on the landing page, click on Edit Inbound Rules button inside Inbound rules section. Now, click on add rule button in the bottom of Inbound rules section. Type would be Custom TCP, Port rage would be 8080, Source would be 0.0.0.0 and click on orange save rule button at the bottom of the page.Now, go to the EC2 instances page and click on instances under instances on the left side menu.Then, click on our instance id link shown in the landing page. Now, copy the address under Public IPv4 address. Now, paste this address in the browser followed by - :8080 which shows us our application.

NOTE: We can terminate the instances when not used to avoid excess charge.
