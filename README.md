# ProcessMirror

## Overview

ProcessMirror is a workflow comparison system that compares an **expected process** with the **process that actually happened**.

Instead of checking only whether a process was completed, ProcessMirror examines how the process was executed.

It identifies:

- Missing steps
- Extra steps
- Repeated steps
- Steps performed in the wrong order
- Completion percentage
- Process compliance
- Overall process deviation

---

## Problem Statement

Organizations often have defined processes that are expected to happen in a particular order.

For example:

```text
Receive Request
      ↓
Validate Request
      ↓
Approve Request
      ↓
Process Request
      ↓
Notify Customer
