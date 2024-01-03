<h1 align="center">BastionCMD Actions</h1>
<p align="center"><strong>Actions used in the program.</strong></p>
This is the folder, where all actions are stored. In this README, it is described what should be in here and what shouldn't.

<h1 align="center">Requirements (so the program doesnt crash)</h1>

- A minimum of 6 actions.
- Each action must include a `action.json` and `action.py` file.
- `action.json` must include the following structure:

```json
{
    "description": "string",
    "needs_connection": true or false,
    "windows": true or false,
    "linux": true or false
}
```

> [!IMPORTANT]
> The description should not be longer than 80 characters, because I can't be bothered to make the description text be generated dynamically in the UI.
>
> If you decide to do this anyway, the program will crash. Not my issue. :trol:

> [!WARNING]
> The description above is partially false. - Jaegerwald

> [!NOTE]
> Remove this joke before 1.0 releases. Or don't. Y'know what you probably should, this isn't professional at all.