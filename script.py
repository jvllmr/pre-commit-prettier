import json
import subprocess


def node_get_package_versions(package_name: str) -> list[str]:
    cmd = ("npm", "view", package_name, "--json")
    output = json.loads(subprocess.check_output(cmd))
    return list(output["time"].keys())


if __name__ == "__main__":
    import pre_commit_mirror_maker.languages  # type: ignore

    NEW_LIST_VERSIONS = {
        **pre_commit_mirror_maker.languages.LIST_VERSIONS,
        "node": node_get_package_versions,
    }
    pre_commit_mirror_maker.languages.LIST_VERSIONS = NEW_LIST_VERSIONS
    from pre_commit_mirror_maker.main import main  # type: ignore

    main(
        [
            ".",
            "--language=node",
            "--package-name=prettier",
            "--types=text",
            "--entry='prettier --write --ignore-unknown'",
            "--id=prettier",
        ]
    )
