# Self-Study Discussion 13.1: Change Data Capture (CDC)

## Prompt Reflection

Change Data Capture (CDC) is a technique used to identify, capture, and propagate changes made to a source database. CDC helps ensure that downstream systems remain synchronized without requiring full data reloads.

A practical example of CDC is a gas utility maintenance and asset management system. The operational database serves as the source of truth and contains information about assets, inspections, technicians, and work orders. Multiple downstream systems may rely on the same data for reporting, analytics, dashboards, and notifications.

### Change Detection

Change detection occurs 