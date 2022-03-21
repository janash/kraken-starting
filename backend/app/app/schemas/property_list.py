from enum import Enum


class PropertyList(str, Enum):
    B1 = 'B1'
    B5 = 'B5'
    EA_delta_SCC = 'EA_delta_SCC'
    HOMO_LUMO_gap = 'HOMO_LUMO_gap'
    IP_delta_SCC = 'IP_delta_SCC'
    alpha = 'alpha'
    cone_angle = 'cone_angle'
    dip_norm = 'dip_norm'
    far_vbur = 'far_vbur'
    far_vtot = 'far_vtot'
    global_electrophilicity_index = 'global_electrophilicity_index'
    lval = 'lval'
    max_delta_qvbur = 'max_delta_qvbur'
    max_delta_qvtot = 'max_delta_qvtot'
    near_vbur = 'near_vbur'
    near_vtot = 'near_vtot'
    nucleophilicity = 'nucleophilicity'
    ovbur_max = 'ovbur_max'
    ovbur_min = 'ovbur_min'
    ovtot_max = 'ovtot_max'
    ovtot_min = 'ovtot_min'
    p_int = 'p_int'
    p_int_area = 'p_int_area'
    p_int_atom = 'p_int_atom'
    p_int_atom_area = 'p_int_atom_area'
    p_int_atom_times_p_int_atom_are = 'ap_int_atom_times_p_int_atom_area'
    p_int_times_p_int_are = 'ap_int_times_p_int_area'
    pyr_alph = 'apyr_alpha'
    pyr_val = 'pyr_val'
    qvbur_max = 'qvbur_max'
    qvbur_min = 'qvbur_min'
    qvtot_max = 'qvtot_max'
    qvtot_min = 'qvtot_min'
    sasa = 'sasa'
    sasa_P = 'sasa_P'
    sasa_volume = 'sasa_volume'
    vbur = 'vbur'
    vtot = 'vtot'
