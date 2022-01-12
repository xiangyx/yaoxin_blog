## 2022/01/07

Question: Visibility binding. When the type of a filed is set as **group** and it should be empty when the referenced filed is empty. But in my configuration it is not.

## 2020/01/10

Two places to upload images
    
    1. Company data (Web add-in portal)
    2. Image Library (Library Module)

How to insert an image, like logo?

    1. Upload the images to Company Data, specifically "Company Logos".
    2. To be able to utilize the images, they need to be either inserted in a newly-created data source or linked to an existing form. 
    3. The rule here is that the value in the 'insert' column should be its exact name as well as its extension, e.g., image.jpeg.
    4. The next step is to create a form containing a Dropdown field that is linked with the data source. (The one storing images)
    5. Attach the form to the selected document (target template) and configure the bindings in the template itself. That is, in the file editor of the template, add the form