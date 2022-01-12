## 20222-01-11

1.  Logo Insertion
    
    - A data source storing logos, link it to a form called CompanyLogo and attach the form to the letter template. Also create two image content controls in header and footer. The problems is that every time creating a new letter a user need to choose a logo from the dropdown box, and the selected one will be inserted into two places, which is not desirable in the sense that the user do not need to choose the logos and two different logos should be inserted respectively.
     
        >Solution: Instead of creating image content controls and adding bindings in the "Element" panel, the easier way is to add *image headers* in "Document" panel, both for logos in header and footer, in which image's settings like width and offsets can be done. In order to insert the two logos at the same time, we can put the data of logos in one row but with distinct column names. So in the image binding we only need to add two references respectively.

    - Also notice that there is an existing filed called LogoInsertion in the UserProfile restored from the backup, and if I change the data source of it from LogoInsertion to CompanyLogo, the logo in header will be put in the right place. The question is why the LogoInsertion filed is different from other ones of type "DropDown" and how to replicate it for the logo in footer.
        
        >Solution: The LogoInsertion filed is restored from the backup, so are the two image header bindings in the letter template. That's why the magic happens when simply change the data source in LogoInsertion. In order not to ask users to choose one option in dropdown box, like the logos, we can add *visibility options* to the field.

    - In [this](https://support.templafy.com/hc/en-us/articles/360014290258-How-to-set-Image-Header-) article, it introduces how to set image header and seems designed for logos on company letterhead. On top of the fields for LogoWidth, it also has fields for the Offset. But the wired thing is the syntax of the binding to an image, e.g., {{UserProfile.Office.Logo.Image}}. Normally, the [syntax](https://support.templafy.com/hc/en-us/articles/360014191417-Image-Binding) is like {{UserProfile.Filed.Column}}, so what is the 'Image' here?

        >Solution: The binding syntax in this article is for Templafy Hive. In Templafy One, the binding syntax is {{UserProfile.FieldName.ColumnName}} or {{Form.FieldName.ColumnName}}
    
    