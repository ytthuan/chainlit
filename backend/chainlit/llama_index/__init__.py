from chainlit.utils import check_module_version

if not check_module_version("llama_index.core", "0.10.27"):
    raise ValueError(
        "Expected LlamaIndex version >= 0.10.15. Run `pip install llama_index --upgrade`"
    )
