# funcshauns  
My Python functions  

## Publishing a New Version to TestPyPI and PyPI  

### Steps for Publishing to TestPyPI (for Testing)  

1. **Increment the Version in pyproject.toml**  
   Open `pyproject.toml` and update the version field under `[project]`.  
   Example:  
   version = "X.Y.Z"  
   Replace `X.Y.Z` with the new version number (e.g., 1.0.1).  

2. **Commit the Version Change**  
   Run the following commands:  
   - Stage the changes:  
     git add pyproject.toml  
   - Commit the changes:  
     git commit -m "Bump version to X.Y.Z"  

3. **Tag the Commit for TestPyPI**  
   Create a tag for TestPyPI with the prefix `test`:  
   git tag -a testX.Y.Z -m "Test releasing X.Y.Z"  
   Replace `X.Y.Z` with the version number (e.g., test1.0.1).  

4. **Push the Test Tag**  
   Push the tag to GitHub:  
   git push origin testX.Y.Z  

5. **Verify the TestPyPI Release**  
   Install the package from TestPyPI to ensure it works as expected:  
   pip install --index-url https://test.pypi.org/simple/ <package-name>  
   Replace `<package-name>` with your package's name.  

### Steps for Publishing to PyPI (for Official Release)  

Once the package has been tested successfully using TestPyPI:  

1. **Ensure the Version is Correct**  
   Verify that the version in `pyproject.toml` matches the version you intend to release to PyPI.  

2. **Tag the Commit for PyPI**  
   Create a tag without the `test` prefix:  
   git tag -a X.Y.Z -m "Release version X.Y.Z"  
   Replace `X.Y.Z` with the version number (e.g., 1.0.1).  

3. **Push the Release Tag**  
   Push the tag to GitHub:  
   git push origin X.Y.Z  

4. **Verify the PyPI Release**  
   - Check the PyPI page to confirm the new version is live:  
     [PyPI Project](https://pypi.org/project/your-package-name/)  
     Replace `your-package-name` with your package's name.  
   - Install the package from PyPI to confirm it works as expected:  
     pip install <package-name>  
     Replace `<package-name>` with your package's name.  
