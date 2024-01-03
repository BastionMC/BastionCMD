<p align="center"><img height="96px" width="224px" src="logo.png">
<h1 align="center">BastionCMD Server</h1>
<p align="center"><strong>The server for BastionCMD</strong></p>
This is the API for BastionCMD, containing all the information that is being pulled from the internet by the client. It contains files about the version, and also data for the actions. You can actually host this server yourself! Here's how you can do that:

<h1 align="center">How to host the API yourself (Using GitHub Pages)</h1>

1. Download BastionCMD's [source](https://www.github.com/BastionMC/BastionCMD), and unzip the folder.
Copy the `server` folder to a location where you can keep it temporarily.

2. [Create a GitHub Pages Repository.](https://docs.github.com/en/pages/quickstart#creating-your-website) After you've done that, use git to [clone that repository to your device]("https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository"). Delete all the files that are in the repository folder.

3. Open the `server` folder that you have saved. Hit <kbd>CTRL</kbd> + <kbd>A</kbd> to select all files, then use <kbd>CTRL</kbd> + <kbd>X</kbd> to cut all the files.

4. Open your repository folder, and use <kbd>CTRL</kbd> + <kbd>V</kbd> to paste the `server` files in your repository.

5. [Commit your changes to the repository](https://github.com/git-guides/git-commit), then [push them](https://github.com/git-guides/git-push). You'll have to wait a bit for GitHub Pages to update, so go to your site's URL and hit refresh until you see this page. **Done! The API should work now.**
    
<p align="center">This tutorial was last updated on the 3rd of January, 2024.</p>

<h1 align="center">Get the client to use your API</h1>

The client will still use the old API. We'll have to modify the client's code to redirect it to the server you have just created. Don't worry, this should be easy; even for someone who doesn't know how to code.

1. Go to the unzipped folder that you've downloaded before. Now copy the `client` folder, and paste it somewhere, where you can find it again, so you can use it later.

(You can, alternatively, also modify the already existing client. Just navigate to it's folder - the tutorial will still work.)

2. In the `client` folder, you'll see a whole bunch of files. We're looking for one named `server.py`. Open this file in a text editor of your choice. (Notepad also works.)

3. Locate the line that says `server_url = "..."`. Change the URL in the quotation marks to your server's URL. Don't forget to add the `/` at the end, its important!

4. Now we'll test if everything works. If you are on Windows, run the `start.bat` file. If you are on Linux, run the `main.py` file. Select one of the actions marked with an `!`, those are the ones that use internet. If they start up without any problem, then congratulations! **Your API is now interacting with the client.**

<p align="center">This tutorial was last updated on the 3rd of January, 2024.</p>