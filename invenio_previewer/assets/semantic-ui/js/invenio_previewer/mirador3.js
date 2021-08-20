import mirador from "mirador";


var miradorInstance = mirador.viewer({
  "id": "mirador-container",
  "manifests": {
    "https://iiif-dev.freizo.org/iiifp.cgi/11121": {
      "provider": "data-futures.org"
    }
  },
  "windows": [
    {
      "loadedManifest": "https://iiif-dev.freizo.org/iiifp.cgi/11121",
      "canvasIndex": 2,
      "thumbnailNavigationPosition": 'far-bottom'
    },
  ]
});
