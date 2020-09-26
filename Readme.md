# Import with Eksport

**Eksport** works no matter your operating system is; Import your external configurations and credentials without extra manual work. It has been built to import AWS IAM configuration by latest downloaded CSV file but should and will be cloud agnostic.

# Installation

    git clone https://github.com/ugurcemozturk/eksport
    pip install -r requirements.txt


# Usage

Simply import your new IAM user credentials from **the latest downloaded CSV** to AWS config file, assumed at home folder, **~/.aws/credentials**
eksport 

    eksport aws

# TO-DO

 - [ ] Add Azure
 - [ ] Add GCP
 - [ ] Override csv path by parameter
 - [ ] Override .aws config path by parameter
 - [ ] Option for file writing, just print to console

## Flow

```mermaid
sequenceDiagram
Eksport ->> OS: Gimme /Downloads path
OS->>Eksport: It's ~/Downloads(i.e.)
Eksport-> Downloads: Gimme latest .csv file
Downloads->> Eksport: Here is the config file: 'iam-profile-name.csv'
Eksport->> AWS Config: Convert csv to TOML and save to ~/.aws/credentials (i.e.)
```

