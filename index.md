# Utility website for serving IIIF manifests

The base URL for this website is <https://baskaufs.github.io/iiif/>.

The links at the top of the page don't work. Click [here](home/) to go to the display home page.

## Links to fellows' Exhibit pages

[Baptismal Ceremony](yella/exhibit)

[Mirador viewer displaying Baptismal Ceremony annotated manifest](https://projectmirador.org/embed/?iiif-content=https://baskaufs.github.io/iiif/yella/baptismal_ceremony.json)

[Annona viewer displaying Baptismal Ceremony annotated manifest](https://ncsu-libraries.github.io/annona/tools/#/display?url=https%3A%2F%2Fbaskaufs.github.io%2Fiiif%2Fyella%2Fbaptismal_ceremony.json&viewtype=iiif-storyboard&manifesturl=&settings=%7B%22fullpage%22%3Atrue%7D)

--------------

[Sala Mpasu Mask](hassan/exhibit)

[Mirador viewer displaying Sala Mpasu Mask annotated manifest](https://projectmirador.org/embed/?iiif-content=https://baskaufs.github.io/iiif/hassan/salampasu_mask.json)

[Annona viewer displaying Sala Mpasu Mask annotated manifest](https://ncsu-libraries.github.io/annona/tools/#/display?url=https%3A%2F%2Fbaskaufs.github.io%2Fiiif%2Fhassan%2Fsalampasu_mask.json&viewtype=iiif-storyboard&manifesturl=&settings=%7B%22fullpage%22%3Atrue%7D)

--------------

[Album du Siège](kim/exhibit)

[Mirador viewer displaying Album du Siége annotated manifest](https://projectmirador.org/embed/?iiif-content=https://baskaufs.github.io/iiif/kim/album_du_siege.json)

[Annona viewer displaying Album du Siége annotated manifest](https://ncsu-libraries.github.io/annona/tools/#/display?url=https%3A%2F%2Fbaskaufs.github.io%2Fiiif%2Fkim%2Falbum_du_siege.json&viewtype=iiif-storyboard&manifesturl=&settings=%7B%22fullpage%22%3Atrue%7D)

## Serving a manifest

To serve a manifest from a subdirectory, append the subdirectory name, followed by the manifest file name. For example:

<https://baskaufs.github.io/iiif/baskauf/getty.json>

## Editing a manifest

An online manifest editor is available at <https://digital.bodleian.ox.ac.uk/manifest-editor/>. To load the manifest, use the manifest URL (as above). Save the manifest in your GitHub directory with a distinctive name and push it to GitHub using GitHub Desktop.

## Validating a manifest

If you are having problems with a manifest, run it through this manifest validator: <https://presentation-validator.iiif.io/>

## Displaying a manifest

Many collections have custom viewers, where the viewer is styled to be consistent with the theme of the institution's website. Here is an example from the Getty Museum collection:

<https://www.getty.edu/art/collection/object/103RAG>

Viewing the [full artwork details](https://www.getty.edu/art/collection/object/103RAG#full-artwork-details) at the bottom of the page gives you access to the IIIF manifest link. You can display that manifest in one of several generic viewers, either directly or by downloading the manifest, hacking it if desired, and serving it from your own website (as I've done below).

### Mirador

Append the manifest URL to the end of 

```
https://projectmirador.org/embed/?iiif-content=
```

For example:

<https://projectmirador.org/embed/?iiif-content=https://baskaufs.github.io/iiif/baskauf/getty.json>

### Universal Viewer

Append the manifest URL to the end of 

```
https://universalviewer.io/uv.html?manifest=
```

For example:

<https://universalviewer.io/uv.html?manifest=https://baskaufs.github.io/iiif/baskauf/getty.json>

### Open Seadragon viewer at Cogapp

Append the manifest URL to the end of

```
https://storiiies.cogapp.com/viewer?manifest=
```

For example:

<https://storiiies.cogapp.com/viewer?manifest=https://storiiies.cogapp.com/holbein/manifest.json>

Manifest served from our website:

<https://storiiies.cogapp.com/viewer?manifest=https://baskaufs.github.io/iiif/baskauf/ambassadors_manifest.json>

NOTE: In this example, the annotations are in a separate file referenced from the manifest:

<https://baskaufs.github.io/iiif/baskauf/ambassador_annotations.json>

Unfortunately, it appears that this viewer will only work with images served from the storiiies.cogapp.com server. So although we can hack this manifest, we can't use it with manifests from our own image server.

## Displaying annotations

Here's an example of a manifest with multiple images and separate annotations for each one:

<https://iiif.harvardartmuseums.org/manifests/object/299843>

If I append this manifest URL to the generic Mirador viewer, I can view the annotations

<https://projectmirador.org/embed/?iiif-content=https://iiif.harvardartmuseums.org/manifests/object/299843>

Click on the hamburger in the upper left.

![hamburger position](hamburger.png)

Then click on the Annotations icon.

![location of annotations icon](annotations_icon.png)

Clicking on a particular annotation will display its box. Clicking on the eye icon will display boxes for all annotations.

![where to click to see annotations](box_annotations.png)

### Creating your own annotations

Here is an annotated image from the Gallery Collection (The Painter and His Pug, print by William Hogarth, 1795, Vanderbilt Fine Arts Gallery 1974.027). The bounding boxes and object recognition were determined by the Google Cloud Vision AI.

<https://projectmirador.org/embed/?iiif-content=https://baskaufs.github.io/iiif/baskauf/painter_dog.json>

Manifest URL:

<https://baskaufs.github.io/iiif/baskauf/painter_dog.json>

Notice that the last section of the manifest has an `otherContent` section with a link to the annotations document (below).

Annotations URL:

<https://baskaufs.github.io/iiif/baskauf/harvard_annotations.json>

Notice that the `selector` values specify the x, y, width, and height of the bounding box. Modifying these values would fix the issues with the bounding box for the person.

## Collecting annotation data

[spreadsheet example](https://github.com/baskaufs/iiif/blob/main/baskauf/annotations/test_annotations.csv)

To use the crop tool, you need the first part of the IIIF image URL. In a manifest, it's the `service` `@id`. Or take any IIIF image URL and it's the part before the location, like `/full/full/0/default.jpg`.

[IIIF crop tool (for getting bounding box coordinates)](https://jbhoward-dublin.github.io/IIIF-imageManipulation/index.html?imageID=https://iiif.library.vanderbilt.edu/iiif/2/gallery%2F1979%2F1979.0321P_copy.tif)

# Exhibit test

[Example of an embedded iFrame](baskauf/iframe_test) created using the Exhibit platform.

[Exhibit website](https://www.exhibit.so/)

[Link to editor](https://exhibit.so/exhibits/create)

[more editors](https://iiif.io/get-started/tools/#exhibition-and-guided-viewing)

# Additional examples

## Yale Center for British Art

Custom viewer

<https://collections.britishart.yale.edu/catalog/tms:390>

Manifest URL

<https://manifests.collections.yale.edu/ycba/obj/390>

## Portain Biblissima

Custom viewer

<https://portail.biblissima.fr/en/ark:/43093/mdata3dcb4570ef3c67e9cf38f6384bf89faf001d54bf>

Manifest URL

<https://digi.ub.uni-heidelberg.de/diglit/iiif/cpgraec222/manifest.json>

## Additional storiiies annotation examples

### Medieval Arab Horsemanship

<https://storiiies.cogapp.com/viewer?manifest=https://storiiies.cogapp.com/qdl/manifest.json>

### Dore's "Dante meets the giants"

<https://storiiies.cogapp.com/viewer?manifest=https://storiiies.cogapp.com/dante/manifest.json>

### Drummand Family

This example uses annotations on multiple canvases.

<https://storiiies.cogapp.com/viewer?manifest=https://storiiies.cogapp.com/ycba/manifest.json>

View manifest in Mirador

<https://projectmirador.org/embed/?iiif-content=https://storiiies.cogapp.com/ycba/manifest.json>
