# Dealing with Jamf

If you are using a new Apple computer purchased by the group (through Northeastern), you will have to deal with the pre-installed Jamf Connect software before you can get started using the computer.

[Last Update: April 2022]

This guide was compiled by Rob Campbell
<br>
<br>

## Contents
1. [About Jamf](/System-Setup/01-Jamf.md#about-jamf)
2. [Getting permission to remove Jamf](/System-Setup/01-Jamf.md#getting-permission-to-remove-jamf)
3. [Removing Jamf requires re-installing macOS](/System-Setup/01-Jamf.md#removing-jamf-requires-re-installing-macos)
<br>

## About Jamf

[Jamf](https://www.jamf.com/home-2/) is an asset management system that Northeastern uses for all Northeastern-owned Apple computers. It lets them remotely access the computer to erase it and/or handle certain administrator priviledges, such as automatic updates. If your computer was purchased with grant money from the group then it is not technically owned by Northeastern, but since we go through Northeastern for the academic purchasing process these computers still arrive with Jamf Connect pre-installed. 

You will know if you have Jamf Connect installed because the software requires you to login to your laptop with your Northeastern username and password via Microsoft Office 365 and you will not be able to change the computer's name, your account username, etc. 

We have had issues with maintaining HOOMD-blue and related software on Jamf managed devices, due to automatic updates and limited administrator priviledges, therefore it is recommended that you get Jamf removed from your laptop before using it for research. **To remove Jamf you MUST get permission from Northeastern first**, otherwise the computer will still be registered on their end of the Jamf asset management system and it will automatically reinstall Jamf Connect.
<br>
<br>
## Getting permission to remove Jamf

To get permission to remove Jamf you need to email IT Services (help@northeastern.edu) and CC Safa, indicating his approval for you to remove Jamf.

Here is an example email template:

> Hello, I am a [graduate student/postdoc/etc] in the Mechanical Engineering Department (NUID #########) working with Prof. Safa Jamali.
>
> Prof. Jamali recently ordered a [Macbook Pro] for my research that arrived with Jamf Connect installed. The group has had issues managing the software we use for our research on Jamf administered devices in the past, and after discussing the situation with Prof. Jamali I would like to have this unmanaged by Jamf.
>
> The computer name is ###############
>
> Please let me know if you need any additional information from me and thank you very much for you help.
</br>
</br>
## Removing Jamf requires re-installing macOS

Once IT confirms that your computer is unmanaged, you can remove Jamf. Unfortunately you do not have permission to do this. Instead you must erase the computer and reinstall macOS. If you have already used your computer, be sure to back it up with TimeMachine or copy any important files to an external hard drive or cloud storage, then follow [Apple's instructions on How to reinstall macOS](https://support.apple.com/en-us/HT204904).
