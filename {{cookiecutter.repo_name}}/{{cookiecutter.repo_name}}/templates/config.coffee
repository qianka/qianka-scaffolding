{% raw -%}
requirejs.config
  paths:
    {% assets "jquery.js" %}"jquery": "{{ ASSET_URL | replace('.js','') }}"{% endassets %}
    {% assets "bootstrap.js" %}"bootstrap": "{{ ASSET_URL | replace('.js','') }}"{% endassets %}

  shim:
    "jquery":
      exports: "$"

    "bootstrap":
      exports: "Bootstrap"
      deps: [
        "jquery"
      ]
{% endraw %}
