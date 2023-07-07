| Problem description | Solution strategies | Examples |
| ---- | ---- | ---- |
|Unable to find/share workflows   | ① Reuse workflow and workflow templates <br> ② Find all reusable GHA in GitHub’s marketplace |① <br>  ② |
|Unable to control the GHA process|① Use conditional expression <br> ② Use concurrency |① <br>  ②|
|Unable to manage multiple compone|① Store multiple workflow files in the ‘.github/workflows’ directory <br> ② Use ‘strategy’ for parallel build and different variation <br> ③ Use a single job with multiple steps <br> ④ Use ‘wildcard’ pattern to configure multiple paths in a step  |① <br>  ②|
|Unable to refer to other components|① Define ‘outputs’ that need to be passed to subsequent jobs <br> ② Use action composition to create a single action then reference it |① <br>  ②|
|Cannot specify/modify actions version | ① Chose the correct version of action <br> ② Use semantic versioning and create a major version for users <br> ③ Move the major version tag (such as v1, v2) <br> ④ Set a dedicate ‘tags’ branch in the ‘on’ attributte |① <br>  ②|
|Unable to get branch name | ① Use variable ${{ github.event.pull_request.base.ref }} <br> ② Use variable ${{ github.ref_name } |① <br>  ②|
|YAML syntax error | ① Directive should be properly indented <br> ② Escape the ‘/’ with a ‘\’ for the filter pattern to work <br> ③ Run multiple commands using a pipe ‘\|’ on the ‘run’ attribute <br> ④ Do not use ‘if: condition’ in YAML because it is no logic attached |① <br>  ②|
|Unable to set/pass environment variable | ① Write the environment variable to the ‘GITHUB_ENV’ file <br> ② Use GitHub secrets to store environment variables <br> ③ Add ‘INPUT_’ to the name of the input variable |① <br>  ②|
|Cannot find/install package | ① Change ‘actions/setup’ to a latest version <br> ② Manually add the package source in a step <br> ③ Add a personal access token with the ‘read:packages’ scope <br> ④ Reference the package’s official documentation |① <br>  ②|
|Unable to configure/share runners | ① Make repositories in one organization to reuse a set of runners <br> ② Use labels to organize self-hosted runners based on their characteristics |① <br>  ②|
|Cannot trigger GHA manually or scheduled | ① Use ‘workflow_dispatch’ and set workflow in the default branch <br> ② Scheduled workflows must run on the latest commit on the default branch <br> ③ Set the shortest interval to run scheduled workflows as 5 minutes |① <br>  ②|
|Unable to check workflow result status | ① Use workflow run API ‘[owner]/[repo]/actions/workflows/[workflowID]/runs’ <br> ② Use the ‘outcome’ property of each step |① <br>  ②|
| Unable to cache steps or artifacts | ① Use ‘actions/cache’ and ‘actions/setup-node@v2.’ actions <br> ② Install package management tools before the cache step |① <br>  ②|
|Cannot access/pass the secrets | ① Reference the GitHub secrets setting guidance <br> ② Reference the environment secret variables in the job <br> ③ Use the ‘gh-secrets-action’ |① <br>  ②|
|GitHub token or PAT error | ① Set GITHUB_TOKEN to expire after the job is finished / Maxi. 24 hours <br> ② Use GITHUB_TOKEN only on default branch <br> ③ Use custom PAT (Personal Access Token) when running on PR branches <br> ④ Use ‘${{ secrets.pat }}’ to manage PAT secret |① <br>  ②|
|Unable to share artifacts  | ① Use the ‘upload-artifact’ and ‘download-artifact’ to share data between jobs <br> ② Use artifact API ‘/actions/artifacts/artifact_id/archive_format' |① <br>  ②|
|Unable to run commands inside container | ① Specify ‘container’ instruction for a job <br> ② Create Dockerfile or docker-compose.yaml then reference it in workflow |① <br>  ②|
| Cannot create Docker image | ① Tag/load the image with the commit sha <br> ② Give docker build the correct path to the Dockerfile <br> ③ Use ‘setup-buildx-action’ step |① <br>  ②|
|Unable to deploy to cloud provider | ① Upgrade cloud provider account from a base free tier to a pay tiered <br> ② Reference the cloud provider’s official documentation <br> ③ Deploy code with rsync over ssh (e.g., use ssh deploy action) |① <br>  ②|
|Continuous deployment issue | ① Keep the ‘app’ within the root project <br> ② Add the service principal with role contributor to the resource group <br> ③ Add files to the repository or make them available on build agent |① <br>  ②|
