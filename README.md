# cirrus-volume
Some happy little volumes

![Perhaps making slightly fewer happy accidents](assets/bob.gif)

### THE RULES  
You cannot write to a CirrusVolume unless you've passed it:
1. A set of sources from which it was created (e.g., another CloudVolume path or a freeform justification like "tracer annotation"). This must be formatted as a `List[str]`, and any sources that haven't been logged previously will be added to the current sources field of the provenance file
2. The motivation for creating the volume (`str`) has been passed or previously logged. A volume can have multiple motivation notes.
3. A `Process` (a code environment & parameters as defined by [provenance-tools](https://github.com/ZettaAI/provenance-tools). The process will be logged unless another process with the same task description has already been logged.
