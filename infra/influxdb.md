# InfluxDB

InfluxDB is a time series based database. The way it works (I think) is by storing the timestamp of change of a metric. For example, consider that the temperature of the CPU is being stored. At time t=1, say the sensor gives a reading of 30. At time t=2 sensor still gives a reading of 30. At t=2.4 the sensor gives a reading of 31, then the db will store this value at this timestamp. Hence the number of datapoints for a sensor with a very high sampling rate will be very high. Hence it is recommended to always group by and calculate the mean.

This document will give a brief overview of the Qarnot InfluxDB structure, tables and their meanings. This document is not meant to be complete.

Tags are used to differentiate instances or versions.git They indicate independent observations. Network and bandwidth related information is not logged. Serialization and collision count are not related to the greco project.

The hierarchy is as follows : qnode -> qbox -> qrad -> qmobo. The parent and child nodes correspondingly refer to the other. The begginning might be either QBOX (in case of Qbox) or its big endian ASCII text.

## Tables

1. instance_slot_state : 
   
   The `Qchunk` and `instances` are the same terms. Instance is used internally, but outside the term is QChunk (which might keep changing). It is a logical entity. It is a part of a motherboard that can execute an instance. Usually there is only one instance per mobo so both are equivalent. but there are certian situations where it is possible to schedule several instances simultaneously to the same mobo (by using pooo with some some extra undocumented stuff). In context of Greco, these are not considered.

   This table is for `instance_slots`. It is a logical space on the motherboard that executes an instance/qchunk.
   
   1. mobo_guid : (tag) " `MOBO-0000-0000-0040-309c236cb16d`
   2. name : (tag) : `SLOT-0000-0000-0040-309c236cb16d-0`
   3. current_instance_number : float
   4. name : string
   5. reserved_for_instance_number : float
   6. serializer_current_instance_guid : string
   7. serializer_mobo_guid : string
   8. serializer_reserved_for_instance_guid : string
   9.  serializer_sampling_time : string
   10. slot_id : float
   11. state : string

2. qbox_state:

    - 8-12 CPU Metrics
   1. core_version : (tag) : Version of the Qbox
   2. qguid : (tag) : The tag of the Qbox. `QBOX-4000-0000-1000-000000000004`
   3. children_nodes : string : ?? Children  network devices. `44415251-adf0-084e-ac62-000000000000`
   4. cluster_tags : string : A Tag showing what type of QBox it is. `qarnot\,8c\,ryzen\,has-virt`
   5. collision_count : string : 
   6. comments : string : Comments
   7. core_version : string : Same as the tag
   8. cpu_available_high : float : 
   9. cpu_available_low : float : 
   10. cpu_count : float : 
   11. current_load : float : 
   12. last_reporting_date : string : 
   13. maintenance_mode : float : Is it undergoing maintainance. Boolean.
   14. maintenance_reason : string : Reason
   15. network_bandwidth : float : 
   16. network_usage : float : 
   17. optimistic_collision_count : float : 
   18. parent_nodes : string :
   19. sampling_time : string : 
   20. serializer_maintenance_time : string : 
   21. serializer_sampling_time : string : 

3. qchunk_state:
   1. name : (tag)
   2. q_mobo : (tag) : `MOBO-0000-0000-0040-309c236cb16d`
   3. qguid : (tag)
   4. state : (tag)
   5. completion_date : string
   6. completion_date_string : string
   7. computed_range : string
   8. cpu_average_ghz : float
   9. cpu_model : string
   10. creation_date : string
   11. creation_date_string : string
   12. failed_range : string
   13. failure_cause : string
   14. initial_range : string
   15. last_reporting_date : string
   16. name : string
   17. priority : float
   18. processed_range : string
   19. q_mobo : string
   20. resources_download_batches : string
   21. sampling_time : string
   22. scaling_cpu_average_ghz : float
   23. scaling_time_compute_ghz : float
   24. serializer_q_mobo : string
   25. serializer_sampling_time : string
   26. serializer_session : string
   27. session : string
   28. state : string
   29. time_compute : float
   30. time_compute_ghz : float
   31. time_download : float
   32. time_environment : float
   33. time_upload : float

4. qjob_state:
   
    This table stores the history log of task creation and completion.

   - 6-19 31-83 : CPU metrics for the Job
   - 2-5 20-29 : Job Metadata
   - 81-83 : Execution Timing
   1. name : (tag) : Na
   2. qguid : (tag)
   3. completion_date : string
   4. completion_date_string : string
   5. computed_range : string
   6. cpu_average_ghz : float
   7. cpu_average_ghz_by_cpu_model_ : float
   8. cpu_average_ghz_by_cpu_model_AMD_Ryzen_7_1700X_Eight-Core_Processor : float
   9.  cpu_average_ghz_by_cpu_model_AMD_Ryzen_7_PRO_1700X_Eight-Core_Processor : float
   10. cpu_average_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-3770K_CPU_@_3.50GHz : float
   11. cpu_average_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4770K_CPU_@_3.50GHz : float
   12. cpu_average_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4771_CPU_@_3.50GHz : float
   13. cpu_average_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4790K_CPU_@_4.00GHz : float
   14. cpu_average_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4790_CPU_@_3.60GHz : float
   15. cpu_average_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-7700K_CPU_@_4.20GHz : float
   16. cpu_average_ghz_by_cpu_model_Intel(R)_Xeon(R)_CPU_E5-2682_v4_@_2.50GHz : float
   17. cpu_average_ghz_by_cpu_model_Intel_Core_Processor_(Broadwell) : float
   18. cpu_average_ghz_by_cpu_model_UNREGISTER_MODEL : float
   19. cpu_average_ghz_by_cpu_model_unknown : float
   20. creation_date : string
   21. creation_date_string : string
   22. custom_guid : string
   23. failed_range : string
   24. failure_cause : string
   25. initial_range : string
   26. last_reporting_date : string
   27. name : string
   28. priority : float
   29. processed_range : string
   30. sampling_time : string
   31. scaling_cpu_average_ghz : float
   32. scaling_cpu_average_ghz_by_cpu_model_AMD_Ryzen_7_1700X_Eight-Core_Processor : float
   33. scaling_cpu_average_ghz_by_cpu_model_AMD_Ryzen_7_PRO_1700X_Eight-Core_Processor : float
   34. scaling_cpu_average_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-3770K_CPU_@_3.50GHz : float
   35. scaling_cpu_average_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4770K_CPU_@_3.50GHz : float
   36. scaling_cpu_average_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4790K_CPU_@_4.00GHz : float
   37. scaling_cpu_average_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4790_CPU_@_3.60GHz : float
   38. scaling_cpu_average_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-7700K_CPU_@_4.20GHz : float
   39. scaling_cpu_average_ghz_by_cpu_model_UNREGISTER_MODEL : float
   40. scaling_time_compute_ghz : float
   41. scaling_time_compute_ghz_by_cpu_model_AMD_Ryzen_7_1700X_Eight-Core_Processor : float
   42. scaling_time_compute_ghz_by_cpu_model_AMD_Ryzen_7_PRO_1700X_Eight-Core_Processor : float
   43. scaling_time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-3770K_CPU_@_3.50GHz : float
   44. scaling_time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4770K_CPU_@_3.50GHz : float
   45. scaling_time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4790K_CPU_@_4.00GHz : float
   46. scaling_time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4790_CPU_@_3.60GHz : float
   47. scaling_time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-7700K_CPU_@_4.20GHz : float
   48. scaling_time_compute_ghz_by_cpu_model_UNREGISTER_MODEL : float
   49. serializer_sampling_time : string
   50. serializer_session : string
   51. session : string
   52. state : string
   53. time_compute : float
   54. time_compute_by_cpu_model_ : float
   55. time_compute_by_cpu_model_AMD_Ryzen_7_1700X_Eight-Core_Processor : float
   56. time_compute_by_cpu_model_AMD_Ryzen_7_PRO_1700X_Eight-Core_Processor : float
   57. time_compute_by_cpu_model_Intel(R)_Core(TM)_i7-3770K_CPU_@_3.50GHz : float
   58. time_compute_by_cpu_model_Intel(R)_Core(TM)_i7-4770K_CPU_@_3.50GHz : float
   59. time_compute_by_cpu_model_Intel(R)_Core(TM)_i7-4771_CPU_@_3.50GHz : float
   60. time_compute_by_cpu_model_Intel(R)_Core(TM)_i7-4790K_CPU_@_4.00GHz : float
   61. time_compute_by_cpu_model_Intel(R)_Core(TM)_i7-4790_CPU_@_3.60GHz : float
   62. time_compute_by_cpu_model_Intel(R)_Core(TM)_i7-7700K_CPU_@_4.20GHz : float
   63. time_compute_by_cpu_model_Intel(R)_Xeon(R)_CPU_E5-2682_v4_@_2.50GHz : float
   64. time_compute_by_cpu_model_Intel_Core_Processor_(Broadwell) : float
   65. time_compute_by_cpu_model_UNREGISTER_MODEL : float
   66. time_compute_by_cpu_model_unknown : float
   67. time_compute_ghz : float
   68. time_compute_ghz_by_cpu_model_ : float
   69. time_compute_ghz_by_cpu_model_AMD_Ryzen_7_1700X_Eight-Core_Processor : float
   70. time_compute_ghz_by_cpu_model_AMD_Ryzen_7_PRO_1700X_Eight-Core_Processor : float
   71. time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-3770K_CPU_@_3.50GHz : float
   72. time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4770K_CPU_@_3.50GHz : float
   73. time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4771_CPU_@_3.50GHz : float
   74. time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4790K_CPU_@_4.00GHz : float
   75. time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4790_CPU_@_3.60GHz : float
   76. time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-7700K_CPU_@_4.20GHz : float
   77. time_compute_ghz_by_cpu_model_Intel(R)_Xeon(R)_CPU_E5-2682_v4_@_2.50GHz : float
   78. time_compute_ghz_by_cpu_model_Intel_Core_Processor_(Broadwell) : float
   79. time_compute_ghz_by_cpu_model_UNREGISTER_MODEL : float
   80. time_compute_ghz_by_cpu_model_unknown : float
   81. time_download : float
   82. time_environment : float
   83. time_upload : float

5. qmobo_state:

    - 8-32 : CPU metrics
   1. cpu : (tag) : Which CPU is used
   2. motherboard_name : (tag) : Which motherboard is used
   3. parent_nodes : (tag) : `44415251-0400-91a3-6f05-000000000000`
   4. qguid : (tag) : `MOBO-0400-9183-87ef-902b34dce964`
   5. state : (tag) : Can be `Debug`, `Unavailable`, `EnvironmentReusable` etc.
   6. type : (tag) : `kvm` or `real`
   7. cpu : string : Which CPU is it?
   8. cpu_burn_usage : float 
   9.  cpu_cores : float
   10. cpu_frequency : float
   11. cpu_instant_power : float
   12. cpu_payload_usage : float
   13. cpu_scaling_frequency : float
   14. cpu_temperature : float
   15. cpu_threads : float
   16. cpu_usage : float
   17. current_command : string : 
   18. current_frame : float
   19. current_task : string
   20. current_task_priority : float
   21. health_status : string : 
   22. ip : string
   23. last_reporting_date : string
   24. machine_state : string
   25. memory_size : float
   26. memory_usage : float
   27. mobo_state  : string
   28. motherboard_cpu_temperature : float
   29. motherboard_name : string
   30. next_frame : float
   31. next_task : string
   32. parent_nodes : string : `44415251-58d8-00d7-8a1f-000000000000`
   33. power_state : float
   34. sampling_time : string
   35. serializer_current_task : string
   36. serializer_next_task : string
   37. serializer_sampling_time : string
   38. stat_bios_count : float
   39. stat_bios_max : float
   40. stat_bios_mean : float
   41. stat_bios_min : float
   42. stat_pxe_count : float
   43. stat_pxe_max : float
   44. stat_pxe_mean : float
   45. stat_pxe_min : float
   46. stat_rx_kb_rate : float
   47. stat_rx_kb_rate_peak : float
   48. stat_rx_mb : float
   49. stat_rx_pkt_dropped : float
   50. stat_rx_pkt_dropped_overall : float
   51. stat_rx_pkt_error : float
   52. stat_rx_pkt_error_overall : float
   53. stat_tx_kb_rate : float
   54. stat_tx_kb_rate_peak : float
   55. stat_tx_mb  : float
   56. stat_tx_pkt_dropped : float
   57. stat_tx_pkt_dropped_overall : float
   58. stat_tx_pkt_error : float
   59. stat_tx_pkt_error_overall : float
   60. type : string : 
   61. qbox : string : `QBOX-8000-0000-0000-000000000002`

6. qnode_state:
   
   Stores the state of the QNode

    - 8-12 : CPU metrics
   1. core_version : (tag) : Version
   2. qguid : (tag) : `NODE-2000-0000-0000-000000000003`
   3. children_nodes : string : `584f4251-2000-0000-0000-000000000002`
   4. collision_count : string : 
   5. comments : string : Comment
   6. connected_apis : string : 
   7. core_version : string : Same as tag
   8. cpu_available_high : float
   9. cpu_available_low : float
   10. cpu_count : float
   11. current_load : float
   12. last_reporting_date : string
   13. maintenance_mode : float
   14. network_bandwidth : float
   15. network_usage : float
   16. optimistic_collision_count : float
   17. sampling_time : string
   18. serializer_maintenance_time : string
   19. serializer_sampling_time : string

7. qrad_state:
   
    - 5-9 : Ambient values
    - 22-29 : Hardware metrics
   1. name : (tag) : Name of the QRad. `0004a39eb7f6000000000`
   2. parent_nodes : (tag) : `584f4251-0000-0000-0000-000000000000`
   3. qguid : (tag) : `QRAD-0400-91a3-d4ff-000000000000`
   4. type : (tag) : Can be `kvm` or `real` or `0004a39eb7f6000000000`
   5. additional_heater_on : float
   6. air_pressure : float
   7. ambient_temperature : float
   8. ambient_temperature_offset : float
   9. c_o2_level : float
   10. heatsink_temperature : float
   11. humidity_level : float
   12. bootloader_version : string
   13. children_nodes : string : `4f424f4d-0400-9ea3-a5da-94de80a6fc53`
   14. firmware_version : string
   15. friendly_name : string
   16. ir_left : float
   17. ir_right : float
   18. last_reporting_date : string
   19. light_left : float
   20. light_right : float
   21. parent_nodes : string : `584f4251-6000-0000-0000-000000000004`
   22. power_consumption_aux : float
   23. power_consumption_aux_watt_hour : float
   24. power_consumption_main : float
   25. power_consumption_main_watt_hour : float
   26. power_instant_aux : float
   27. power_instant_main : float
   28. power_instant_main : float
   29. sampling_time : string
   30. serializer_sampling_time : string
   31. target_temperature : float : Target temperature of the QRad
   32. type : string

8. qtask_state:

    A Qtask represents successive snapshots of running qjobs.

    - 3-20 : Task Metadata
    - 31-57 : CPU info for that task
    - 58-60 : Environment time
   1. name : (tag) : `docker.base.config>docker.base>docker-mining>money\ money\ money\ qualif` or replace by `prod` at end.
   2. qguid : (tag) : `docker.base.config>docker.base>blender.base>blender-2.79>SQ_02_P02_V22_PACK.blend`
   3. attached_node : string : 
   4. cpu_average_ghz : float
   5. creation_date : string
   6. creation_date_string : string
   7. custom_guid : string
   8. failed_range : string
   9. initial_range : string
   10. last_reporting_date : string
   11. name : string : 
   12. parent_node : string
   13. parent_task : string
   14. priority : float
   15. processed_range : string
   16. progress_compute : float
   17. progress_download : float
   18. progress_upload : float
   19. root_node : string
   20. sampling_time : string
   21. scaling_time_compute_ghz : float
   22. serializer_attached_node : string
   23. serializer_parent_node : string
   24. serializer_parent_task : string
   25. serializer_root_node : string
   26. serializer_sampling_time : string
   27. serializer_session : string
   28. serializer_task : string
   29. session : string
   30. task : string
   31. time_compute : float
   32. time_compute_by_cpu_model_ : float
   33. time_compute_by_cpu_model_AMD_Ryzen_7_1700X_Eight-Core_Processor : float
   34. time_compute_by_cpu_model_AMD_Ryzen_7_PRO_1700X_Eight-Core_Processor : float
   35. time_compute_by_cpu_model_Intel(R)_Core(TM)_i7-3770K_CPU_@_3.50GHz : float
   36. time_compute_by_cpu_model_Intel(R)_Core(TM)_i7-4770K_CPU_@_3.50GHz : float
   37. time_compute_by_cpu_model_Intel(R)_Core(TM)_i7-4771_CPU_@_3.50GHz : float
   38. time_compute_by_cpu_model_Intel(R)_Core(TM)_i7-4790K_CPU_@_4.00GHz : float
   39. time_compute_by_cpu_model_Intel(R)_Core(TM)_i7-4790_CPU_@_3.60GHz : float
   40. time_compute_by_cpu_model_Intel(R)_Core(TM)_i7-7700K_CPU_@_4.20GHz : float
   41. time_compute_by_cpu_model_Intel(R)_Xeon(R)_CPU_E5-2682_v4_@_2.50GHz : float
   42. time_compute_by_cpu_model_Intel_Core_Processor_(Broadwell) : float
   43. time_compute_by_cpu_model_UNREGISTER_MODEL : float
   44. time_compute_by_cpu_model_unknown : float
   45. time_compute_ghz : float
   46. time_compute_ghz_by_cpu_model_ : float
   47. time_compute_ghz_by_cpu_model_AMD_Ryzen_7_1700X_Eight-Core_Processor : float
   48. time_compute_ghz_by_cpu_model_AMD_Ryzen_7_PRO_1700X_Eight-Core_Processor : float
   49. time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-3770K_CPU_@_3.50GHz : float
   50. time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4770K_CPU_@_3.50GHz : float
   51. time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4771_CPU_@_3.50GHz : float
   52. time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4790K_CPU_@_4.00GHz : float
   53. time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-4790_CPU_@_3.60GHz : float
   54. time_compute_ghz_by_cpu_model_Intel(R)_Core(TM)_i7-7700K_CPU_@_4.20GHz : float
   55. time_compute_ghz_by_cpu_model_Intel(R)_Xeon(R)_CPU_E5-2682_v4_@_2.50GHz : float
   56. time_compute_ghz_by_cpu_model_Intel_Core_Processor_(Broadwell) : float
   57. time_compute_ghz_by_cpu_model_unknown : float
   58. time_download : float
   59. time_environment : float
   60. time_upload : float


9.  transfer_hisory:

    Stores the transfers from qbox to CEPH or vice versa.

    - 7-9 13-17 : Transfer characteristics
    1. qbox : (tag) : `QBOX-2000-0000-0000-000000000002`
    2. qguid : (tag) : 
    3. session : (tag) : `QSES-0101-0211-ba3c-db63e64c1aaf`
    4. task : (tag) : `QSES-0101-0211-ba3c-db63e64c1aaf`
    5. actually_transferred_size : float
    6. attached_node : string : Attached QBOX relating to the transfer (transfer happes directly from qbox to ceph)
    7. cached_data_size : float
    8. completion_date_string : string
    9. creation_date_string : string
    10. serializer_sampling_time : string
    11. serializer_session : string
    12. serializer_task : string
    13. state : string
    14. time_transfer_sec : float
    15. transfer_direction : string
    16. transfer_size : float
    17. transfer_type : string
