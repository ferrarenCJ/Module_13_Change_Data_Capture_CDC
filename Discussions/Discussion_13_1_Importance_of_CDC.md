# Required Discussion 13.1: The Importance of Change Data Capture (CDC)

One use case where Change Data Capture (CDC) would be highly beneficial is a gas utility maintenance and asset management system. In this type of system, a database stores information about assets, inspections, technicians, and work orders. The source of truth could be a MySQL database that supports daily operational activities, while downstream databases support reporting, analytics, and dashboards.

**Change detection** occurs whenever a work order is created, updated, or closed. For example, if a technician completes an inspection and updates a work order status from "Open" to "Completed," the CDC process identifies that change. **Change capture** records information about the modification, such as the affected record, timestamp, and type of operation. **Change propagation** then transfers the change to downstream systems, such as a MongoDB analytics database, a Redis cache used for dashboard performance, or a Cassandra database used for large-scale historical reporting.

One useful CDC technique would be **audit columns**, such as `created_time` and `updated_time`. These fields make it easy to determine which records have changed since the last synchronization. Another approach is **table deltas**, where snapshots of the data are compared to identify inserts, updates, and deletions. While this method provides accurate results, it requires additional storage to maintain multiple snapshots.

To keep systems synchronized, the organization could use **periodic queries** that run every few minutes. These queries would check for records with newer timestamps and propagate those changes to downstream databases. This approach has relatively low overhead and helps ensure that operational, reporting, and analytics systems remain consistent without requiring a full database reload each time data changes.

Overall, CDC improves data consistency, reduces processing