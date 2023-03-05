release-0.2
=======
# Contributing to OSC&R

We would love for you to contribute to the OSC&R project and help make it even better than it is today!
As a contributor, here are the guidelines we would like you to follow:

 - [Code of Conduct](#coc)
 - [Question or Problem?](#question)
 - [Issues and Bugs](#issue)
 - [Feature Requests](#feature)
 - [Submission Guidelines](#submit)
 - [Coding Rules](#rules)
 - [Commit Message Guidelines](#commit)
 - [Signing the CLA](#cla)


## <a name="coc"></a> Code of Conduct

Help us keep OSC&R open and inclusive.
Please read and follow our [Code of Conduct][coc].


## <a name="question"></a> Got a Question or Problem?

Do not open issues for general support questions as we want to keep GitHub issues for bug reports and feature requests.
Instead, we recommend using our [Slack Channel](https://osc-r.slack.com/) to ask support-related questions.

To save your and our time, we will systematically close all issues that are requests for general support and redirect people to [Slack](https://osc-r.slack.com/).


## <a name="issue"></a> Found a Bug?

If you find a bug / logical flaw / missing link in the documentation, you can help us by [submitting an issue](#submit-issue) to our [GitHub Repository][github].
Even better, you can [submit a Pull Request](#submit-pr) with a fix.


## <a name="feature"></a> Missing a Feature / technique / control?
You can *request* an addition by [submitting an issue](#submit-issue) to our GitHub Repository.
If you would like to *implement* a new addition to the model, please consider the size of the change in order to determine the right steps to proceed:

* For a **Major addition**, first open an issue and outline your proposal so that it can be discussed.
  This process allows us to better coordinate our efforts, prevent duplication of work, and help you to craft the change so that it is successfully accepted into the project.

  **Note**: Adding a new topic to the documentation, or significantly re-writing a topic, counts as a major feature.

* **Small additions** can be crafted and directly [submitted as a Pull Request](#submit-pr).


## <a name="submit"></a> Submission Guidelines

### <a name="signing-code"></a> Code Signing

Code signing is mandatory to make a contribution to OCS&R. Learn more about how to sign code in the following article [About commit signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification).

Commits that are not signed will not be approved and merged.

### <a name="submit-issue"></a> Submitting an Issue

Before you submit an issue, please search the issue tracker. An issue for your problem might already exist and the discussion might inform you of workarounds readily available.

We want to fix all the issues / add more content as soon as possible, but before adding anything, we would like to confirm it aligns with the OSC&R patterns and presents itself as a beneficial addition to the model.

You can file new issues by selecting from our [new issue templates](https://github.com/pbom-dev/OSCAR/issues/new/choose) and filling out the issue template.


### <a name="submit-pr"></a> Submitting a Pull Request (PR)

Before you submit your Pull Request (PR) consider the following guidelines:

1. Search [GitHub](https://github.com/pbom-dev/OSCAR/pulls) for an open or closed PR that relates to your submission.
   You don't want to duplicate existing efforts.

2. Be sure that an issue describes the problem you are fixing, or documents the design for the addition you would like to add.
   Discussing the design upfront helps to ensure that we are ready to accept your work.

3. [Fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) the pbom-dev/OSCAR repo.

4. In your forked repository, make your changes in a new git branch:

     ```shell
     git checkout -b my-fix-branch main
     ```

5. Create your content,
 
7. Follow our [Coding Rules](#rules).

8. Commit your changes using a descriptive commit message that follows our [commit message conventions](#commit).
   Adherence to these conventions is necessary because release notes are automatically generated from these messages.

     ```shell
     git commit --all
     ```
    Note: the optional commit `-a` command line option will automatically "add" and "rm" edited files.

9.  Push your branch to GitHub:

    ```shell
    git push origin my-fix-branch
    ```

10. In GitHub, send a pull request to `OSCAR:main`.

### Reviewing a Pull Request

The OSC&R team reserves the right not to accept pull requests from community members who have not been good citizens of the community. Such behavior includes not following the [OSC&R code of conduct](https://github.com/pbom-dev/OSCAR/code-of-conduct) and applies within or outside of OSC&R managed channels.

#### Addressing review feedback

If we ask for changes via code reviews then:

1. Make the required updates to the code.

2. Create a fixup commit and push to your GitHub repository (this will update your Pull Request):

    ```shell
    git commit --all --fixup HEAD
    git push
    ```

    For more info on working with fixup commits see [here](docs/FIXUP_COMMITS.md).

That's it! Thank you for your contribution!


##### Updating the commit message

A reviewer might often suggest changes to a commit message (for example, to add more context for a change or adhere to our [commit message guidelines](#commit)).
In order to update the commit message of the last commit on your branch:

1. Check out your branch:

    ```shell
    git checkout my-fix-branch
    ```

We would love for you to contribute to the OSC&R project and help make it even better than it is today! We have place for developers and content creators.
[Slack]: https://osc-r.slack.com/
[coc]: https://github.com/pbom-dev/OSCAR/CODE_OF_CONDUCT.md
[github]: https://github.com/pbom-dev/OSCAR/
