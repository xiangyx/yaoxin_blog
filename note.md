#   Templafy One

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


#   Templafy Hive

## 2022//01/18
- General Information
    - What is it?
      - Having modular design offers exceptional flexibility
    - Access levels in Templafy Hive tenants
        1. tenant user
        2. tenant admin
        3. tenant owner
        4. space owner (Only when **Spaces module** activated)
    - What can tenant owners do?
      - Access the Admin Center of Templafy tenant
      - Manage modules
      - Assign admin licenses
      - Revoke admin licenses
    - Features & Functionalities Hive have but One haven't
      - Binding Validation
      - Binding Functions
      - Document API
      - Templafy App connector
      - ...
- Account & Authentication
- Resources
  - Managing data sources
    - How to create ? 
        1.  Create the data source
        2.  Create the Schema of the data source (The structure)
        3.  Add data source items (The content)
  - System generated data sources
    - Prerequisites
      - Admin access and Library/Email modules enabled
    - They're managed by Templafy and cannot be deleted.
    - Type
      - Color themes
      - Languages
      - Fonts
      - Translations
- Dynamics
  - After toggling the switch "Enable as template" in Dynamics Designer, we can get started in dynamic configurations. For example, if we can go to Forms tab to create gating questions for the user to answer, or from the Element tab create bindings to forms or data sources. The dynamic designer has 4 different tabs.
    - Settings
      - enable the document as a template, i.e., activating dynamics.
      - enable Document Content Updater
      - ...
    - Form
      - create and edit from fields
    - Document
      - set document metadata, including 1) Color theme, 2) Custom Document, 3) Control/Create the document settings.
    - Element
      - create binds linking to forms or company's data sources/resources

## 2020/01/20

  1. How to set Document Name in Hive?
     1. Add "Document Name (Dynamics Templates)" in Document tab, and create a binding to the field (TextBox) of which you want to use the value as the title of your document, e.g., {{Form.DocumentName}}. However, be careful that this way only works when downloading documents from WebApp or Desktop in Word
     2. If we want to set the title for a document created from Word, when choosing the option "Open in Word" and then save the document, then use the "Document Property" - "Title".

## 2020/01/21

  1. In Hive, Date does not have a separate data source but its format is stored in Translations for different languages.
  2. In One, the syntax of translation is *Translations.Term*, whereas it is *Translate("Term")*.
  3. In One, the syntax of date is *Form.Date* since it has a separate date form. In Hive, firstly we need to add a date filed in the form, then based on the needed date format and document language the binding of date is *FormatDateTime(Form.Date,Translate("DateGeneral"), DocumentLanguage)*.