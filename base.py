 public | res_company                                   | table | odoo
 public | res_company_users_rel                         | table | odoo
 public | res_config                                    | table | odoo
 public | res_config_installer                          | table | odoo
 public | res_config_settings                           | table | odoo
 public | res_country                                   | table | odoo
 public | res_country_group                             | table | odoo
 public | res_country_res_country_group_rel             | table | odoo
 public | res_country_state                             | table | odoo
 public | res_currency                                  | table | odoo
 public | res_currency_rate                             | table | odoo
 public | res_font                                      | table | odoo
 public | res_groups                                    | table | odoo
 public | res_groups_action_rel                         | table | odoo
 public | res_groups_implied_rel                        | table | odoo
 public | res_groups_report_rel                         | table | odoo
 public | res_groups_users_rel                          | table | odoo
 public | res_lang                                      | table | odoo
 public | res_partner                                   | table | odoo
 public | res_partner_bank                              | table | odoo
 public | res_partner_bank_type                         | table | odoo
 public | res_partner_bank_type_field                   | table | odoo
 public | res_partner_category                          | table | odoo
 public | res_partner_res_partner_category_rel          | table | odoo
 public | res_partner_title                             | table | odoo
 public | res_request_link                              | table | odoo
 public | res_users                                     | table | odoo
 public | rule_group_rel                                | table | odoo
 public | wizard_ir_model_menu_create                   | table | odoo
 public | wkf                                           | table | odoo
 public | wkf_activity                                  | table | odoo
 public | wkf_instance                                  | table | odoo
 public | wkf_transition                                | table | odoo
 public | wkf_triggers                                  | table | odoo
 public | wkf_witm_trans                                | table | odoo
 public | wkf_workitem                                  | table | odoo
(130 rows)

materiales=# drop table materiales_recepcion cascade;
NOTICE:  drop cascades to 2 other objects
DETAIL:  drop cascades to constraint materiales_recepcion_detalle_recepcion_id_fkey on table materiales_recepcion_detalle 
drop cascades to constraint materiales_detallerec_recepcion_id_fkey on table materiales_detallerec
DROP TABLE
materiales=# \dt
                           List of relations
 Schema |                     Name                      | Type  | Owner
--------+-----------------------------------------------+-------+-------
 public | base_import_import                            | table | odoo
 public | base_import_tests_models_char                 | table | odoo
 public | base_import_tests_models_char_noreadonly      | table | odoo
 public | base_import_tests_models_char_readonly        | table | odoo
 public | base_import_tests_models_char_required        | table | odoo
 public | base_import_tests_models_char_states          | table | odoo
 public | base_import_tests_models_char_stillreadonly   | table | odoo
 public | base_import_tests_models_m2o                  | table | odoo
 public | base_import_tests_models_m2o_related          | table | odoo
 public | base_import_tests_models_m2o_required         | table | odoo
 public | base_import_tests_models_m2o_required_related | table | odoo
 public | base_import_tests_models_o2m                  | table | odoo
 public | base_import_tests_models_o2m_child            | table | odoo
 public | base_import_tests_models_preview              | table | odoo
 public | base_language_export                          | table | odoo
 public | base_language_import                          | table | odoo
 public | base_language_install                         | table | odoo
 public | base_module_configuration                     | table | odoo
 public | base_module_update                            | table | odoo
 public | base_module_upgrade                           | table | odoo
 public | base_update_translations                      | table | odoo
 public | bus_bus                                       | table | odoo
 public | change_password_user                          | table | odoo
 public | change_password_wizard                        | table | odoo
 public | im_chat_message                               | table | odoo
 public | im_chat_presence                              | table | odoo
 public | im_chat_session                               | table | odoo
 public | im_chat_session_res_users_rel                 | table | odoo
 public | ir_act_client                                 | table | odoo
 public | ir_act_report_xml                             | table | odoo
 public | ir_act_server                                 | table | odoo
 public | ir_act_url                                    | table | odoo
 public | ir_act_window                                 | table | odoo
 public | ir_act_window_group_rel                       | table | odoo
 public | ir_act_window_view                            | table | odoo
 public | ir_actions                                    | table | odoo
 public | ir_actions_todo                               | table | odoo
 public | ir_attachment                                 | table | odoo
 public | ir_config_parameter                           | table | odoo
 public | ir_config_parameter_groups_rel                | table | odoo
 public | ir_cron                                       | table | odoo
 public | ir_default                                    | table | odoo
 public | ir_exports                                    | table | odoo
 public | ir_exports_line                               | table | odoo
 public | ir_fields_converter                           | table | odoo
 public | ir_filters                                    | table | odoo
 public | ir_logging                                    | table | odoo
 public | ir_mail_server                                | table | odoo
 public | ir_model                                      | table | odoo
 public | ir_model_access                               | table | odoo
 public | ir_model_constraint                           | table | odoo
 public | ir_model_data                                 | table | odoo
 public | ir_model_fields                               | table | odoo
 public | ir_model_fields_group_rel                     | table | odoo
 public | ir_model_relation                             | table | odoo
 public | ir_module_category                            | table | odoo
 public | ir_module_module                              | table | odoo
 public | ir_module_module_dependency                   | table | odoo
 public | ir_property                                   | table | odoo
 public | ir_rule                                       | table | odoo
 public | ir_sequence                                   | table | odoo
 public | ir_sequence_type                              | table | odoo
 public | ir_server_object_lines                        | table | odoo
 public | ir_translation                                | table | odoo
 public | ir_ui_menu                                    | table | odoo
 public | ir_ui_menu_group_rel                          | table | odoo
 public | ir_ui_view                                    | table | odoo
 public | ir_ui_view_custom                             | table | odoo
 public | ir_ui_view_group_rel                          | table | odoo
 public | ir_values                                     | table | odoo
 public | it_materiales_informacion                     | table | odoo
 public | it_materiales_producto                        | table | odoo
 public | it_materiales_ubicaciones                     | table | odoo
 public | materiales_compras                            | table | odoo
 public | materiales_criterios                          | table | odoo
 public | materiales_detalle                            | table | odoo
 public | materiales_detallerec                         | table | odoo
 public | materiales_evaluacion                         | table | odoo
 public | materiales_informacion                        | table | odoo
 public | materiales_parametros                         | table | odoo
 public | materiales_producto                           | table | odoo
 public | materiales_productos                          | table | odoo
 public | materiales_programa                           | table | odoo
 public | materiales_proveedor                          | table | odoo
 public | materiales_recepcion_detalle                  | table | odoo
 public | materiales_service                            | table | odoo
 public | materiales_ubicaciones                        | table | odoo
 public | multi_company_default                         | table | odoo
 public | osv_memory_autovacuum                         | table | odoo
 public | rel_modules_langexport                        | table | odoo
 public | rel_server_actions                            | table | odoo
 public | report                                        | table | odoo
 public | report_paperformat                            | table | odoo
 public | res_bank                                      | table | odoo
 public | res_company                                   | table | odoo
 public | res_company_users_rel                         | table | odoo
 public | res_config                                    | table | odoo
 public | res_config_installer                          | table | odoo
 public | res_config_settings                           | table | odoo
 public | res_country                                   | table | odoo
 public | res_country_group                             | table | odoo
 public | res_country_res_country_group_rel             | table | odoo
 public | res_country_state                             | table | odoo
 public | res_currency                                  | table | odoo
 public | res_currency_rate                             | table | odoo
 public | res_font                                      | table | odoo
 public | res_groups                                    | table | odoo
 public | res_groups_action_rel                         | table | odoo
 public | res_groups_implied_rel                        | table | odoo
 public | res_groups_report_rel                         | table | odoo
 public | res_groups_users_rel                          | table | odoo
 public | res_lang                                      | table | odoo
 public | res_partner                                   | table | odoo
 public | res_partner_bank                              | table | odoo
 public | res_partner_bank_type                         | table | odoo
 public | res_partner_bank_type_field                   | table | odoo
 public | res_partner_category                          | table | odoo
 public | res_partner_res_partner_category_rel          | table | odoo
 public | res_partner_title                             | table | odoo
 public | res_request_link                              | table | odoo
 public | res_users                                     | table | odoo
 public | rule_group_rel                                | table | odoo
 public | wizard_ir_model_menu_create                   | table | odoo
 public | wkf                                           | table | odoo
 public | wkf_activity                                  | table | odoo
 public | wkf_instance                                  | table | odoo
 public | wkf_transition                                | table | odoo
 public | wkf_triggers                                  | table | odoo
 public | wkf_witm_trans                                | table | odoo
 public | wkf_workitem                                  | table | odoo
(130 rows)

materiales=# drop table materiales_detallerec;
DROP TABLE
materiales=# \dt
                           List of relations
 Schema |                     Name                      | Type  | Owner
--------+-----------------------------------------------+-------+-------
 public | base_import_import                            | table | odoo
 public | base_import_tests_models_char                 | table | odoo
 public | base_import_tests_models_char_noreadonly      | table | odoo
 public | base_import_tests_models_char_readonly        | table | odoo
 public | base_import_tests_models_char_required        | table | odoo
 public | base_import_tests_models_char_states          | table | odoo
 public | base_import_tests_models_char_stillreadonly   | table | odoo
 public | base_import_tests_models_m2o                  | table | odoo
 public | base_import_tests_models_m2o_related          | table | odoo
 public | base_import_tests_models_m2o_required         | table | odoo
 public | base_import_tests_models_m2o_required_related | table | odoo
 public | base_import_tests_models_o2m                  | table | odoo
 public | base_import_tests_models_o2m_child            | table | odoo
 public | base_import_tests_models_preview              | table | odoo
 public | base_language_export                          | table | odoo
 public | base_language_import                          | table | odoo
 public | base_language_install                         | table | odoo
 public | base_module_configuration                     | table | odoo
 public | base_module_update                            | table | odoo
 public | base_module_upgrade                           | table | odoo
 public | base_update_translations                      | table | odoo
 public | bus_bus                                       | table | odoo
 public | change_password_user                          | table | odoo
 public | change_password_wizard                        | table | odoo
 public | im_chat_message                               | table | odoo
 public | im_chat_presence                              | table | odoo
 public | im_chat_session                               | table | odoo
 public | im_chat_session_res_users_rel                 | table | odoo
 public | ir_act_client                                 | table | odoo
 public | ir_act_report_xml                             | table | odoo
 public | ir_act_server                                 | table | odoo
 public | ir_act_url                                    | table | odoo
 public | ir_act_window                                 | table | odoo
 public | ir_act_window_group_rel                       | table | odoo
 public | ir_act_window_view                            | table | odoo
 public | ir_actions                                    | table | odoo
 public | ir_actions_todo                               | table | odoo
 public | ir_attachment                                 | table | odoo
 public | ir_config_parameter                           | table | odoo
 public | ir_config_parameter_groups_rel                | table | odoo
 public | ir_cron                                       | table | odoo
 public | ir_default                                    | table | odoo
 public | ir_exports                                    | table | odoo
 public | ir_exports_line                               | table | odoo
 public | ir_fields_converter                           | table | odoo
 public | ir_filters                                    | table | odoo
 public | ir_logging                                    | table | odoo
 public | ir_mail_server                                | table | odoo
 public | ir_model                                      | table | odoo
 public | ir_model_access                               | table | odoo
 public | ir_model_constraint                           | table | odoo
 public | ir_model_data                                 | table | odoo
 public | ir_model_fields                               | table | odoo
 public | ir_model_fields_group_rel                     | table | odoo
 public | ir_model_relation                             | table | odoo
 public | ir_module_category                            | table | odoo
 public | ir_module_module                              | table | odoo
 public | ir_module_module_dependency                   | table | odoo
 public | ir_property                                   | table | odoo
 public | ir_rule                                       | table | odoo
 public | ir_sequence                                   | table | odoo
 public | ir_sequence_type                              | table | odoo
 public | ir_server_object_lines                        | table | odoo
 public | ir_translation                                | table | odoo
 public | ir_ui_menu                                    | table | odoo
 public | ir_ui_menu_group_rel                          | table | odoo
 public | ir_ui_view                                    | table | odoo
 public | ir_ui_view_custom                             | table | odoo
 public | ir_ui_view_group_rel                          | table | odoo
 public | ir_values                                     | table | odoo
 public | it_materiales_informacion                     | table | odoo
 public | it_materiales_producto                        | table | odoo
 public | it_materiales_ubicaciones                     | table | odoo
 public | materiales_compras                            | table | odoo
 public | materiales_criterios                          | table | odoo
 public | materiales_detalle                            | table | odoo
 public | materiales_detallerec                         | table | odoo
 public | materiales_evaluacion                         | table | odoo
 public | materiales_informacion                        | table | odoo
 public | materiales_parametros                         | table | odoo
 public | materiales_producto                           | table | odoo
 public | materiales_productos                          | table | odoo
 public | materiales_programa                           | table | odoo
 public | materiales_proveedor                          | table | odoo
 public | materiales_recepcion                          | table | odoo
 public | materiales_recepcion_detalle                  | table | odoo
 public | materiales_service                            | table | odoo
 public | materiales_ubicaciones                        | table | odoo
 public | multi_company_default                         | table | odoo
 public | osv_memory_autovacuum                         | table | odoo
 public | rel_modules_langexport                        | table | odoo
 public | rel_server_actions                            | table | odoo
 public | report                                        | table | odoo
 public | report_paperformat                            | table | odoo
 public | res_bank                                      | table | odoo
 public | res_company                                   | table | odoo
 public | res_company_users_rel                         | table | odoo
 public | res_config                                    | table | odoo
 public | res_config_installer                          | table | odoo
 public | res_config_settings                           | table | odoo
 public | res_country                                   | table | odoo
 public | res_country_group                             | table | odoo
 public | res_country_res_country_group_rel             | table | odoo
 public | res_country_state                             | table | odoo
 public | res_currency                                  | table | odoo
 public | res_currency_rate                             | table | odoo
 public | res_font                                      | table | odoo
 public | res_groups                                    | table | odoo
 public | res_groups_action_rel                         | table | odoo
 public | res_groups_implied_rel                        | table | odoo
 public | res_groups_report_rel                         | table | odoo
 public | res_groups_users_rel                          | table | odoo
 public | res_lang                                      | table | odoo
 public | res_partner                                   | table | odoo
 public | res_partner_bank                              | table | odoo
 public | res_partner_bank_type                         | table | odoo
 public | res_partner_bank_type_field                   | table | odoo
 public | res_partner_category                          | table | odoo
 public | res_partner_res_partner_category_rel          | table | odoo
 public | res_partner_title                             | table | odoo
 public | res_request_link                              | table | odoo
 public | res_users                                     | table | odoo
 public | rule_group_rel                                | table | odoo
 public | wizard_ir_model_menu_create                   | table | odoo
 public | wkf                                           | table | odoo
 public | wkf_activity                                  | table | odoo
 public | wkf_instance                                  | table | odoo
 public | wkf_transition                                | table | odoo
 public | wkf_triggers                                  | table | odoo
 public | wkf_witm_trans                                | table | odoo
 public | wkf_workitem                                  | table | odoo
(131 rows)

materiales=# drop table materiales_detallerec cascade;
DROP TABLE
materiales=# \dt'
                           List of relations
 Schema |                     Name                      | Type  | Owner
--------+-----------------------------------------------+-------+-------
 public | base_import_import                            | table | odoo
 public | base_import_tests_models_char                 | table | odoo
 public | base_import_tests_models_char_noreadonly      | table | odoo
 public | base_import_tests_models_char_readonly        | table | odoo
 public | base_import_tests_models_char_required        | table | odoo
 public | base_import_tests_models_char_states          | table | odoo
 public | base_import_tests_models_char_stillreadonly   | table | odoo
 public | base_import_tests_models_m2o                  | table | odoo
 public | base_import_tests_models_m2o_related          | table | odoo
 public | base_import_tests_models_m2o_required         | table | odoo
 public | base_import_tests_models_m2o_required_related | table | odoo
 public | base_import_tests_models_o2m                  | table | odoo
 public | base_import_tests_models_o2m_child            | table | odoo
 public | base_import_tests_models_preview              | table | odoo
 public | base_language_export                          | table | odoo
 public | base_language_import                          | table | odoo
 public | base_language_install                         | table | odoo
 public | base_module_configuration                     | table | odoo
 public | base_module_update                            | table | odoo
 public | base_module_upgrade                           | table | odoo
 public | base_update_translations                      | table | odoo
 public | bus_bus                                       | table | odoo
 public | change_password_user                          | table | odoo
 public | change_password_wizard                        | table | odoo
 public | im_chat_message                               | table | odoo
 public | im_chat_presence                              | table | odoo
 public | im_chat_session                               | table | odoo
 public | im_chat_session_res_users_rel                 | table | odoo
 public | ir_act_client                                 | table | odoo
 public | ir_act_report_xml                             | table | odoo
 public | ir_act_server                                 | table | odoo
 public | ir_act_url                                    | table | odoo
 public | ir_act_window                                 | table | odoo
 public | ir_act_window_group_rel                       | table | odoo
 public | ir_act_window_view                            | table | odoo
 public | ir_actions                                    | table | odoo
 public | ir_actions_todo                               | table | odoo
 public | ir_attachment                                 | table | odoo
 public | ir_config_parameter                           | table | odoo
 public | ir_config_parameter_groups_rel                | table | odoo
 public | ir_cron                                       | table | odoo
 public | ir_default                                    | table | odoo
 public | ir_exports                                    | table | odoo
 public | ir_exports_line                               | table | odoo
 public | ir_fields_converter                           | table | odoo
 public | ir_filters                                    | table | odoo
 public | ir_logging                                    | table | odoo
 public | ir_mail_server                                | table | odoo
 public | ir_model                                      | table | odoo
 public | ir_model_access                               | table | odoo
 public | ir_model_constraint                           | table | odoo
 public | ir_model_data                                 | table | odoo
 public | ir_model_fields                               | table | odoo
 public | ir_model_fields_group_rel                     | table | odoo
 public | ir_model_relation                             | table | odoo
 public | ir_module_category                            | table | odoo
 public | ir_module_module                              | table | odoo
 public | ir_module_module_dependency                   | table | odoo
 public | ir_property                                   | table | odoo
 public | ir_rule                                       | table | odoo
 public | ir_sequence                                   | table | odoo
 public | ir_sequence_type                              | table | odoo
 public | ir_server_object_lines                        | table | odoo
 public | ir_translation                                | table | odoo
 public | ir_ui_menu                                    | table | odoo
 public | ir_ui_menu_group_rel                          | table | odoo
 public | ir_ui_view                                    | table | odoo
 public | ir_ui_view_custom                             | table | odoo
 public | ir_ui_view_group_rel                          | table | odoo
 public | ir_values                                     | table | odoo
 public | it_materiales_informacion                     | table | odoo
 public | it_materiales_producto                        | table | odoo
 public | it_materiales_ubicaciones                     | table | odoo
 public | materiales_compras                            | table | odoo
 public | materiales_criterios                          | table | odoo
 public | materiales_detalle                            | table | odoo
 public | materiales_evaluacion                         | table | odoo
 public | materiales_informacion                        | table | odoo
 public | materiales_parametros                         | table | odoo
 public | materiales_producto                           | table | odoo
 public | materiales_productos                          | table | odoo
 public | materiales_programa                           | table | odoo
 public | materiales_proveedor                          | table | odoo
 public | materiales_recepcion                          | table | odoo
 public | materiales_recepcion_detalle                  | table | odoo
 public | materiales_service                            | table | odoo
 public | materiales_ubicaciones                        | table | odoo
 public | multi_company_default                         | table | odoo
 public | osv_memory_autovacuum                         | table | odoo
 public | rel_modules_langexport                        | table | odoo
 public | rel_server_actions                            | table | odoo
 public | report                                        | table | odoo
 public | report_paperformat                            | table | odoo
 public | res_bank                                      | table | odoo
 public | res_company                                   | table | odoo
 public | res_company_users_rel                         | table | odoo
 public | res_config                                    | table | odoo
 public | res_config_installer                          | table | odoo
 public | res_config_settings                           | table | odoo
 public | res_country                                   | table | odoo
 public | res_country_group                             | table | odoo
 public | res_country_res_country_group_rel             | table | odoo
 public | res_country_state                             | table | odoo
 public | res_currency                                  | table | odoo
 public | res_currency_rate                             | table | odoo
 public | res_font                                      | table | odoo
 public | res_groups                                    | table | odoo
 public | res_groups_action_rel                         | table | odoo
 public | res_groups_implied_rel                        | table | odoo
 public | res_groups_report_rel                         | table | odoo
 public | res_groups_users_rel                          | table | odoo
 public | res_lang                                      | table | odoo
 public | res_partner                                   | table | odoo
 public | res_partner_bank                              | table | odoo
 public | res_partner_bank_type                         | table | odoo
 public | res_partner_bank_type_field                   | table | odoo
 public | res_partner_category                          | table | odoo
 public | res_partner_res_partner_category_rel          | table | odoo
 public | res_partner_title                             | table | odoo
 public | res_request_link                              | table | odoo
 public | res_users                                     | table | odoo
 public | rule_group_rel                                | table | odoo
 public | wizard_ir_model_menu_create                   | table | odoo
 public | wkf                                           | table | odoo
 public | wkf_activity                                  | table | odoo
 public | wkf_instance                                  | table | odoo
 public | wkf_transition                                | table | odoo
 public | wkf_triggers                                  | table | odoo
 public | wkf_witm_trans                                | table | odoo
 public | wkf_workitem                                  | table | odoo
(130 rows)

materiales=# drop table materiales_compras;
DROP TABLE
materiales=# drop table materiales_compras cascade;
DROP TABLE
materiales=# /dt
materiales-# \dt
                           List of relations
 Schema |                     Name                      | Type  | Owner
--------+-----------------------------------------------+-------+-------
 public | base_import_import                            | table | odoo
 public | base_import_tests_models_char                 | table | odoo
 public | base_import_tests_models_char_noreadonly      | table | odoo
 public | base_import_tests_models_char_readonly        | table | odoo
 public | base_import_tests_models_char_required        | table | odoo
 public | base_import_tests_models_char_states          | table | odoo
 public | base_import_tests_models_char_stillreadonly   | table | odoo
 public | base_import_tests_models_m2o                  | table | odoo
 public | base_import_tests_models_m2o_related          | table | odoo
 public | base_import_tests_models_m2o_required         | table | odoo
 public | base_import_tests_models_m2o_required_related | table | odoo
 public | base_import_tests_models_o2m                  | table | odoo
 public | base_import_tests_models_o2m_child            | table | odoo
 public | base_import_tests_models_preview              | table | odoo
 public | base_language_export                          | table | odoo
 public | base_language_import                          | table | odoo
 public | base_language_install                         | table | odoo
 public | base_module_configuration                     | table | odoo
 public | base_module_update                            | table | odoo
 public | base_module_upgrade                           | table | odoo
 public | base_update_translations                      | table | odoo
 public | bus_bus                                       | table | odoo
 public | change_password_user                          | table | odoo
 public | change_password_wizard                        | table | odoo
 public | im_chat_message                               | table | odoo
 public | im_chat_presence                              | table | odoo
 public | im_chat_session                               | table | odoo
 public | im_chat_session_res_users_rel                 | table | odoo
 public | ir_act_client                                 | table | odoo
 public | ir_act_report_xml                             | table | odoo
 public | ir_act_server                                 | table | odoo
 public | ir_act_url                                    | table | odoo
 public | ir_act_window                                 | table | odoo
 public | ir_act_window_group_rel                       | table | odoo
 public | ir_act_window_view                            | table | odoo
 public | ir_actions                                    | table | odoo
 public | ir_actions_todo                               | table | odoo
 public | ir_attachment                                 | table | odoo
 public | ir_config_parameter                           | table | odoo
 public | ir_config_parameter_groups_rel                | table | odoo
 public | ir_cron                                       | table | odoo
 public | ir_default                                    | table | odoo
 public | ir_exports                                    | table | odoo
 public | ir_exports_line                               | table | odoo
 public | ir_fields_converter                           | table | odoo
 public | ir_filters                                    | table | odoo
 public | ir_logging                                    | table | odoo
 public | ir_mail_server                                | table | odoo
 public | ir_model                                      | table | odoo
 public | ir_model_access                               | table | odoo
 public | ir_model_constraint                           | table | odoo
 public | ir_model_data                                 | table | odoo
 public | ir_model_fields                               | table | odoo
 public | ir_model_fields_group_rel                     | table | odoo
 public | ir_model_relation                             | table | odoo
 public | ir_module_category                            | table | odoo
 public | ir_module_module                              | table | odoo
 public | ir_module_module_dependency                   | table | odoo
 public | ir_property                                   | table | odoo
 public | ir_rule                                       | table | odoo
 public | ir_sequence                                   | table | odoo
 public | ir_sequence_type                              | table | odoo
 public | ir_server_object_lines                        | table | odoo
 public | ir_translation                                | table | odoo
 public | ir_ui_menu                                    | table | odoo
 public | ir_ui_menu_group_rel                          | table | odoo
 public | ir_ui_view                                    | table | odoo
 public | ir_ui_view_custom                             | table | odoo
 public | ir_ui_view_group_rel                          | table | odoo
 public | ir_values                                     | table | odoo
 public | it_materiales_informacion                     | table | odoo
 public | it_materiales_producto                        | table | odoo
 public | it_materiales_ubicaciones                     | table | odoo
 public | materiales_compras                            | table | odoo
 public | materiales_criterios                          | table | odoo
 public | materiales_detalle                            | table | odoo
 public | materiales_detallerec                         | table | odoo
 public | materiales_evaluacion                         | table | odoo
 public | materiales_informacion                        | table | odoo
 public | materiales_parametros                         | table | odoo
 public | materiales_producto                           | table | odoo
 public | materiales_productos                          | table | odoo
 public | materiales_programa                           | table | odoo
 public | materiales_proveedor                          | table | odoo
 public | materiales_recepcion                          | table | odoo
 public | materiales_recepcion_detalle                  | table | odoo
 public | materiales_service                            | table | odoo
 public | materiales_ubicaciones                        | table | odoo
 public | multi_company_default                         | table | odoo
 public | osv_memory_autovacuum                         | table | odoo
 public | rel_modules_langexport                        | table | odoo
 public | rel_server_actions                            | table | odoo
 public | report                                        | table | odoo
 public | report_paperformat                            | table | odoo
 public | res_bank                                      | table | odoo
 public | res_company                                   | table | odoo
 public | res_company_users_rel                         | table | odoo
 public | res_config                                    | table | odoo
 public | res_config_installer                          | table | odoo
 public | res_config_settings                           | table | odoo
 public | res_country                                   | table | odoo
 public | res_country_group                             | table | odoo
 public | res_country_res_country_group_rel             | table | odoo
 public | res_country_state                             | table | odoo
 public | res_currency                                  | table | odoo
 public | res_currency_rate                             | table | odoo
 public | res_font                                      | table | odoo
 public | res_groups                                    | table | odoo
 public | res_groups_action_rel                         | table | odoo
 public | res_groups_implied_rel                        | table | odoo
 public | res_groups_report_rel                         | table | odoo
 public | res_groups_users_rel                          | table | odoo
 public | res_lang                                      | table | odoo
 public | res_partner                                   | table | odoo
 public | res_partner_bank                              | table | odoo
 public | res_partner_bank_type                         | table | odoo
 public | res_partner_bank_type_field                   | table | odoo
 public | res_partner_category                          | table | odoo
 public | res_partner_res_partner_category_rel          | table | odoo
 public | res_partner_title                             | table | odoo
 public | res_request_link                              | table | odoo
 public | res_users                                     | table | odoo
 public | rule_group_rel                                | table | odoo
 public | wizard_ir_model_menu_create                   | table | odoo
 public | wkf                                           | table | odoo
 public | wkf_activity                                  | table | odoo
 public | wkf_instance                                  | table | odoo
 public | wkf_transition                                | table | odoo
 public | wkf_triggers                                  | table | odoo
 public | wkf_witm_trans                                | table | odoo
 public | wkf_workitem                                  | table | odoo
(131 rows)
materiales-#
  Try Docker Debug for seamless, persistent debugging tools in any container or image → docker debug db
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
Successfully copied 164kB to 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
odoo
PS C:\Users\52453\Documents\it_materiales> docker exec -it db bash
root@409874dd1107:/# \dt
bash: dt: command not found
root@409874dd1107:/# psql -U odoo materiales 
psql (9.6.24)
Type "help" for help.

materiales=# \dt
                           List of relations
 Schema |                     Name                      | Type  | Owner
--------+-----------------------------------------------+-------+-------
 public | base_import_import                            | table | odoo
 public | base_import_tests_models_char                 | table | odoo
 public | base_import_tests_models_char_noreadonly      | table | odoo
 public | base_import_tests_models_char_readonly        | table | odoo
 public | base_import_tests_models_char_required        | table | odoo
 public | base_import_tests_models_char_states          | table | odoo
 public | base_import_tests_models_char_stillreadonly   | table | odoo
 public | base_import_tests_models_m2o                  | table | odoo
 public | base_import_tests_models_m2o_related          | table | odoo
 public | base_import_tests_models_m2o_required         | table | odoo
 public | base_import_tests_models_m2o_required_related | table | odoo
 public | base_import_tests_models_o2m                  | table | odoo
 public | base_import_tests_models_o2m_child            | table | odoo
 public | base_import_tests_models_preview              | table | odoo
 public | base_language_export                          | table | odoo
 public | base_language_import                          | table | odoo
 public | base_language_install                         | table | odoo
 public | base_module_configuration                     | table | odoo
 public | base_module_update                            | table | odoo
 public | base_module_upgrade                           | table | odoo
 public | base_update_translations                      | table | odoo
 public | bus_bus                                       | table | odoo
 public | change_password_user                          | table | odoo
 public | change_password_wizard                        | table | odoo
 public | im_chat_message                               | table | odoo
 public | im_chat_presence                              | table | odoo
 public | im_chat_session                               | table | odoo
 public | im_chat_session_res_users_rel                 | table | odoo
 public | ir_act_client                                 | table | odoo
 public | ir_act_report_xml                             | table | odoo
 public | ir_act_server                                 | table | odoo
 public | ir_act_url                                    | table | odoo
 public | ir_act_window                                 | table | odoo
 public | ir_act_window_group_rel                       | table | odoo
 public | ir_act_window_view                            | table | odoo
 public | ir_actions                                    | table | odoo
 public | ir_actions_todo                               | table | odoo
 public | ir_attachment                                 | table | odoo
 public | ir_config_parameter                           | table | odoo
 public | ir_config_parameter_groups_rel                | table | odoo
 public | ir_cron                                       | table | odoo
 public | ir_default                                    | table | odoo
 public | ir_exports                                    | table | odoo
 public | ir_exports_line                               | table | odoo
 public | ir_fields_converter                           | table | odoo
 public | ir_filters                                    | table | odoo
 public | ir_logging                                    | table | odoo
 public | ir_mail_server                                | table | odoo
 public | ir_model                                      | table | odoo
 public | ir_model_access                               | table | odoo
 public | ir_model_constraint                           | table | odoo
 public | ir_model_data                                 | table | odoo
 public | ir_model_fields                               | table | odoo
 public | ir_model_fields_group_rel                     | table | odoo
 public | ir_model_relation                             | table | odoo
 public | ir_module_category                            | table | odoo
 public | ir_module_module                              | table | odoo
 public | ir_module_module_dependency                   | table | odoo
 public | ir_property                                   | table | odoo
 public | ir_rule                                       | table | odoo
 public | ir_sequence                                   | table | odoo
 public | ir_sequence_type                              | table | odoo
 public | ir_server_object_lines                        | table | odoo
 public | ir_translation                                | table | odoo
 public | ir_ui_menu                                    | table | odoo
 public | ir_ui_menu_group_rel                          | table | odoo
 public | ir_ui_view                                    | table | odoo
 public | ir_ui_view_custom                             | table | odoo
 public | ir_ui_view_group_rel                          | table | odoo
 public | ir_values                                     | table | odoo
 public | it_materiales_informacion                     | table | odoo
 public | it_materiales_producto                        | table | odoo
 public | it_materiales_ubicaciones                     | table | odoo
 public | materiales_compras                            | table | odoo
 public | materiales_criterios                          | table | odoo
 public | materiales_detalle                            | table | odoo
 public | materiales_detallerec                         | table | odoo
 public | materiales_evaluacion                         | table | odoo
 public | materiales_informacion                        | table | odoo
 public | materiales_parametros                         | table | odoo
 public | materiales_producto                           | table | odoo
 public | materiales_productos                          | table | odoo
 public | materiales_programa                           | table | odoo
 public | materiales_proveedor                          | table | odoo
 public | materiales_recepcion                          | table | odoo
 public | materiales_recepcion_detalle                  | table | odoo
 public | materiales_service                            | table | odoo
 public | materiales_ubicaciones                        | table | odoo
 public | multi_company_default                         | table | odoo
 public | osv_memory_autovacuum                         | table | odoo
 public | rel_modules_langexport                        | table | odoo
 public | rel_server_actions                            | table | odoo
 public | report                                        | table | odoo
 public | report_paperformat                            | table | odoo
 public | res_bank                                      | table | odoo
 public | res_company                                   | table | odoo
 public | res_company_users_rel                         | table | odoo
 public | res_config                                    | table | odoo
 public | res_config_installer                          | table | odoo
 public | res_config_settings                           | table | odoo
 public | res_country                                   | table | odoo
 public | res_country_group                             | table | odoo
 public | res_country_res_country_group_rel             | table | odoo
 public | res_country_state                             | table | odoo
 public | res_currency                                  | table | odoo
 public | res_currency_rate                             | table | odoo
 public | res_font                                      | table | odoo
 public | res_groups                                    | table | odoo
 public | res_groups_action_rel                         | table | odoo
 public | res_groups_implied_rel                        | table | odoo
 public | res_groups_report_rel                         | table | odoo
 public | res_groups_users_rel                          | table | odoo
 public | res_lang                                      | table | odoo
 public | res_partner                                   | table | odoo
 public | res_partner_bank                              | table | odoo
 public | res_partner_bank_type                         | table | odoo
 public | res_partner_bank_type_field                   | table | odoo
 public | res_partner_category                          | table | odoo
 public | res_partner_res_partner_category_rel          | table | odoo
 public | res_partner_title                             | table | odoo
 public | res_request_link                              | table | odoo
 public | res_users                                     | table | odoo
 public | rule_group_rel                                | table | odoo
 public | wizard_ir_model_menu_create                   | table | odoo
 public | wkf                                           | table | odoo
 public | wkf_activity                                  | table | odoo
 public | wkf_instance                                  | table | odoo
 public | wkf_transition                                | table | odoo
 public | wkf_triggers                                  | table | odoo
 public | wkf_witm_trans                                | table | odoo
 public | wkf_workitem                                  | table | odoo
(131 rows)

materiales=# SELECT * FROM materiales_compras WHERE id = 2;
 id | status | create_uid | create_date | name | fecha | write_uid | proveedor_id | write_date | total 
----+--------+------------+-------------+------+-------+-----------+--------------+------------+-------
(0 rows)

materiales=# SELECT * FROM materiales_compras;
 id | status | create_uid | create_date | name | fecha | write_uid | proveedor_id | write_date | total 
----+--------+------------+-------------+------+-------+-----------+--------------+------------+-------
(0 rows)

materiales=# \dt
                           List of relations
 Schema |                     Name                      | Type  | Owner
--------+-----------------------------------------------+-------+-------
 public | base_import_import                            | table | odoo
 public | base_import_tests_models_char                 | table | odoo
 public | base_import_tests_models_char_noreadonly      | table | odoo
 public | base_import_tests_models_char_readonly        | table | odoo
 public | base_import_tests_models_char_required        | table | odoo
 public | base_import_tests_models_char_states          | table | odoo
 public | base_import_tests_models_char_stillreadonly   | table | odoo
 public | base_import_tests_models_m2o                  | table | odoo
 public | base_import_tests_models_m2o_related          | table | odoo
 public | base_import_tests_models_m2o_required         | table | odoo
 public | base_import_tests_models_m2o_required_related | table | odoo
 public | base_import_tests_models_o2m                  | table | odoo
 public | base_import_tests_models_o2m_child            | table | odoo
 public | base_import_tests_models_preview              | table | odoo
 public | base_language_export                          | table | odoo
 public | base_language_import                          | table | odoo
 public | base_language_install                         | table | odoo
 public | base_module_configuration                     | table | odoo
 public | base_module_update                            | table | odoo
 public | base_module_upgrade                           | table | odoo
 public | base_update_translations                      | table | odoo
 public | bus_bus                                       | table | odoo
 public | change_password_user                          | table | odoo
 public | change_password_wizard                        | table | odoo
 public | im_chat_message                               | table | odoo
 public | im_chat_presence                              | table | odoo
 public | im_chat_session                               | table | odoo
 public | im_chat_session_res_users_rel                 | table | odoo
 public | ir_act_client                                 | table | odoo
 public | ir_act_report_xml                             | table | odoo
 public | ir_act_server                                 | table | odoo
 public | ir_act_url                                    | table | odoo
 public | ir_act_window                                 | table | odoo
 public | ir_act_window_group_rel                       | table | odoo
 public | ir_act_window_view                            | table | odoo
 public | ir_actions                                    | table | odoo
 public | ir_actions_todo                               | table | odoo
 public | ir_attachment                                 | table | odoo
 public | ir_config_parameter                           | table | odoo
 public | ir_config_parameter_groups_rel                | table | odoo
 public | ir_cron                                       | table | odoo
 public | ir_default                                    | table | odoo
 public | ir_exports                                    | table | odoo
 public | ir_exports_line                               | table | odoo
 public | ir_fields_converter                           | table | odoo
 public | ir_filters                                    | table | odoo
 public | ir_logging                                    | table | odoo
 public | ir_mail_server                                | table | odoo
 public | ir_model                                      | table | odoo
 public | ir_model_access                               | table | odoo
 public | ir_model_constraint                           | table | odoo
 public | ir_model_data                                 | table | odoo
 public | ir_model_fields                               | table | odoo
 public | ir_model_fields_group_rel                     | table | odoo
 public | ir_model_relation                             | table | odoo
 public | ir_module_category                            | table | odoo
 public | ir_module_module                              | table | odoo
 public | ir_module_module_dependency                   | table | odoo
 public | ir_property                                   | table | odoo
 public | ir_rule                                       | table | odoo
 public | ir_sequence                                   | table | odoo
 public | ir_sequence_type                              | table | odoo
 public | ir_server_object_lines                        | table | odoo
 public | ir_translation                                | table | odoo
 public | ir_ui_menu                                    | table | odoo
 public | ir_ui_menu_group_rel                          | table | odoo
 public | ir_ui_view                                    | table | odoo
 public | ir_ui_view_custom                             | table | odoo
 public | ir_ui_view_group_rel                          | table | odoo
 public | ir_values                                     | table | odoo
 public | it_materiales_informacion                     | table | odoo
 public | it_materiales_producto                        | table | odoo
 public | it_materiales_ubicaciones                     | table | odoo
 public | materiales_compras                            | table | odoo
 public | materiales_criterios                          | table | odoo
 public | materiales_detalle                            | table | odoo
 public | materiales_detallerec                         | table | odoo
 public | materiales_evaluacion                         | table | odoo
 public | materiales_informacion                        | table | odoo
 public | materiales_parametros                         | table | odoo
 public | materiales_producto                           | table | odoo
 public | materiales_productos                          | table | odoo
 public | materiales_programa                           | table | odoo
 public | materiales_proveedor                          | table | odoo
 public | materiales_recepcion                          | table | odoo
 public | materiales_recepcion_detalle                  | table | odoo
 public | materiales_service                            | table | odoo
 public | materiales_ubicaciones                        | table | odoo
 public | multi_company_default                         | table | odoo
 public | osv_memory_autovacuum                         | table | odoo
 public | rel_modules_langexport                        | table | odoo
 public | rel_server_actions                            | table | odoo
 public | report                                        | table | odoo
 public | report_paperformat                            | table | odoo
 public | res_bank                                      | table | odoo
 public | res_company                                   | table | odoo
 public | res_company_users_rel                         | table | odoo
 public | res_config                                    | table | odoo
 public | res_config_installer                          | table | odoo
 public | res_config_settings                           | table | odoo
 public | res_country                                   | table | odoo
 public | res_country_group                             | table | odoo
 public | res_country_res_country_group_rel             | table | odoo
 public | res_country_state                             | table | odoo
 public | res_currency                                  | table | odoo
 public | res_currency_rate                             | table | odoo
 public | res_font                                      | table | odoo
 public | res_groups                                    | table | odoo
 public | res_groups_action_rel                         | table | odoo
 public | res_groups_implied_rel                        | table | odoo
 public | res_groups_report_rel                         | table | odoo
 public | res_groups_users_rel                          | table | odoo
 public | res_lang                                      | table | odoo
 public | res_partner                                   | table | odoo
 public | res_partner_bank                              | table | odoo
 public | res_partner_bank_type                         | table | odoo
 public | res_partner_bank_type_field                   | table | odoo
 public | res_partner_category                          | table | odoo
 public | res_partner_res_partner_category_rel          | table | odoo
 public | res_partner_title                             | table | odoo
 public | res_request_link                              | table | odoo
 public | res_users                                     | table | odoo
 public | rule_group_rel                                | table | odoo
 public | wizard_ir_model_menu_create                   | table | odoo
 public | wkf                                           | table | odoo
 public | wkf_activity                                  | table | odoo
 public | wkf_instance                                  | table | odoo
 public | wkf_transition                                | table | odoo
 public | wkf_triggers                                  | table | odoo
 public | wkf_witm_trans                                | table | odoo
 public | wkf_workitem                                  | table | odoo
(131 rows)

materiales=# SELECT * FROM materiales_detallerec;
 id | create_uid | create_date | cantidad | producto | recepcion_id | costo_real | write_date | write_uid | compra_id 
----+------------+-------------+----------+----------+--------------+------------+------------+-----------+-----------    
(0 rows)
materiales=#
  Try Docker Debug for seamless, persistent debugging tools in any container or image → docker debug db
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
odoo
PS C:\Users\52453\Documents\it_materiales> docker cp ../it_materiales 46fab124aaf9:/mnt/extra-addons/.
Successfully copied 179kB to 46fab124aaf9:/mnt/extra-addons/.
PS C:\Users\52453\Documents\it_materiales> docker restart odoo
odoo


        <!-- Vista tipo form del modelo materiales.compras -->
        <record model="ir.ui.view" id="materiales_compras_form">
            <field name="name">materiales.compras.form</field>
            <field name="model">materiales.comprados</field>
            <field name="type">form</field>
            <field name="arch" type="xml">
                <form string="Compras">
                    <header>
                        <field name="status" widget="statusbar"/>
                        <button name="action_confirm" type="object" string="Confirmar compra" status="creado" class="oe_highlight"/>
                        <!-- <button name="action_receive" type="object" string="Recibir" status="pedido" class="oe_highlight"/> -->
                        <button name="action_cancel" type="object" string="Cancelar" status="creado,pedido,recibido" class="oe_highlight"/>
                    </header>
                    <sheet>
                        <group string="Información de Compra">
                            <field name="name"/> 
                            <field name="fecha"/>
                            <field name="proveedor_id"/>
                            <field name="total"/>
                            <field name="totalr"/>
                        </group>
                        <notebook>
                            <page string="Detalles de Compra">
                                <field name="detalle_ids" widget="one2many_list">
                                    <tree editable="bottom">
                                        <field name="requisicion_id"/>
                                        <field name="producto"/>
                                        <field name="cantidad"/>
                                        <field name="costo_estimado"/>
                                        <field name="costo_real"/>
                                        <field name="factura"/>
                                    </tree>
                                </field>
                            </page>
                        </notebook>
                    </sheet>
                </form>
            </field>
        </record>