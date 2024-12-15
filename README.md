# archived

prettier made some changes that breaks plugins entirely

---

# prettier mirror

Mirror of prettier package for pre-commit.

For pre-commit: see https://github.com/pre-commit/pre-commit

For prettier: see https://github.com/prettier/prettier

### Using prettier with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/pre-commit/mirrors-prettier
  rev: "" # Use the sha / tag you want to point at
  hooks:
    - id: prettier
```

_note_: only prettier versions >= 2.1.0 are supported

### Usage with plugins

When using plugins with `prettier` you'll need to declare them under
`additional_dependencies`. And a `.prettierrc.cjs` config file. For example:

```yaml
- repo: https://github.com/pre-commit/mirrors-prettier
  rev: "" # Use the sha / tag you want to point at
  hooks:
    - id: prettier
      additional_dependencies:
        - prettier@3.4.2
        - prettier-plugin-toml
```

```javascript
const config = {
  plugins: [require.resolve("prettier-plugin-toml")],
};

module.exports = config;
```

This way prettier is able to find the plugin in pre-commit's environment.
If your project already includes a JavaScript project and it has the desired plugin installed, you don't need the `.prettierrc.cjs` file in your project and you use can your preferred way of configuring prettier instead.

### Restrict covered files

By default, all files are passed to `prettier`, if you want to limit the
file list, adjust `types` / `types_or` / `files`:

```yaml
- id: prettier
  types_or: [css, javascript]
```
