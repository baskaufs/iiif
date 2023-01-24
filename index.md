# Utility website for serving IIIF manifests

The base URL for this website is <https://baskaufs.github.io/iiif/>.

## Serving a manifest

To serve a manifest from a subdirectory, append the subdirectory name, followed by the manifest file name. For example:

<https://baskaufs.github.io/iiif/baskauf/getty.json>

## Displaying a manifest

You can display a manifest in one of several generic viewers.

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

<https://storiiies.cogapp.com/viewer?manifest=https://baskaufs.github.io/iiif/baskauf/ambassadors_manifest.json>

NOTE: In this example, the annotations are in a separate file referenced from the manifest:

<https://baskaufs.github.io/iiif/baskauf/ambassador_annotations.json>

