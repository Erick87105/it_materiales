# -*- coding: utf-8 -*-
from openerp import models, fields, api
from datetime import datetime

class Productos(models.Model):
    _name = 'materiales.productos'
    _description = 'Productos del Inventario'

    foto = fields.Binary(string='Foto del Producto')
    clave = fields.Char(string='Clave', readonly=True)
    name = fields.Char(string='Nombre del Producto o Servicio')
    marca = fields.Char(string='Marca')
    modelo = fields.Char(string='Modelo')
    serie = fields.Char(string='Identificación de Serie')
    
    CATEGORIA = [
        ('inmuebles', 'Bienes Inmuebles'),
        ('muebles', 'Bienes Muebles'),
        ('medico', 'Equipo Médico y de Laboratorio'),
        ('transporte', 'Equipo de Transporte'),
        ('maquinaria', 'Maquinaria, Otros Equipos y Herramientas'),
        ('biologicos', 'Activos Biológicos'),
        ('servicios', 'Servicios'),
    ]
    categoria = fields.Selection(CATEGORIA, string='Categoría', required=True)
    
    subcategoria = fields.Selection([
        ('viviendas', 'Viviendas'),
        ('edificios', 'Edificios No Habitacionales'),
        ('infraestructura', 'Infraestructura'),
        ('otros_inmuebles', 'Otros Bienes Inmuebles'),
        ('muebles_oficina', 'Muebles de Oficina y Estantería'),
        ('muebles_excepcion', 'Muebles Excepto De Oficina y Estantería'),
        ('computo', 'Equipo de Cómputo y Tecnologías de la Información'),
        ('otros_muebles', 'Otros Mobiliarios y Equipos de Administración'),
        ('educacional', 'Mobiliario y Equipo Educacional y Recreativo'),
        ('audiovisuales', 'Equipos y Aparatos Audiovisuales'),
        ('deportivos', 'Aparatos Deportivos'),
        ('fotografia_video', 'Cámaras Fotográficas y de Video'),
        ('equipo_medico', 'Equipo Médico y de Laboratorio'),
        ('instrumental_medico', 'Instrumental Médico y de Laboratorio'),
        ('automoviles', 'Automóviles y Equipo Terrestre'),
        ('carrocerias', 'Carrocerías y Remolques'),
        ('aeroespacial', 'Equipo Aeroespacial'),
        ('ferroviario', 'Equipo Ferroviario'),
        ('embarcaciones', 'Embarcaciones'),
        ('otros_transporte', 'Otros Equipos de Transporte'),
        ('agropecuario', 'Maquinaria y Equipo Agropecuario'),
        ('industrial', 'Maquinaria y Equipo Industrial'),
        ('construccion', 'Maquinaria y Equipo de Construcción'),
        ('aire_acondicionado', 'Sistemas de Aire Acondicionado, Calefacción y de Refrigeración Industrial y Comercial'),
        ('telecomunicacion', 'Equipo de Comunicación y Telecomunicación'),
        ('electrico', 'Equipos de Generación Eléctrica, Aparatos y Accesorios Eléctricos'),
        ('herramientas', 'Herramientas y Máquinas-Herramienta'),
        ('otros_equipos', 'Otros Equipos'),
        ('bovinos', 'Bovinos'),
        ('porcinos', 'Porcinos'),
        ('aves', 'Aves'),
        ('ovinos_caprinos', 'Ovinos y Caprinos'),
        ('peces', 'Peces y Acuicultura'),
        ('equinos', 'Equinos'),
        ('zoologico', 'Especies Menores y de Zoológico'),
        ('arboles_plantas', 'Árboles y Plantas'),
        ('otros_biologicos', 'Otros Activos Biológicos'),
        ('mantenimiento_infraestructura', 'Mantenimiento de Infraestructura'),
        ('consultoria_academica', 'Consultoría Académica'),
        ('soporte_tecnico', 'Soporte Técnico'),
        ('capacitacion', 'Capacitación y Desarrollo'),
        ('limpieza', 'Servicios de Limpieza'),
        ('seguridad', 'Servicios de Seguridad'),
        ('administrativos', 'Servicios Administrativos'),
    ], string='Subcategoría', required=True)

    cantidad = fields.Integer(string='Cantidad', default=1)
    anos_vida_util = fields.Integer(string='Años de Vida Útil', required=True)
    depreciacion_anual = fields.Float(string='% de Depreciación Anual', required=True)
    valor_actual = fields.Float(string='Valor Actual')
    valor_depreciado = fields.Float(string='Valor Depreciado', compute='_compute_valor_depreciado', store=True)
    
    activo = fields.Boolean(string='Activo')
    estatus = fields.Char(string='Estado')
    observaciones = fields.Text(string='Observaciones')
    descripcion = fields.Text(string='Descripción')
    proveedor_id = fields.Many2one('materiales.proveedor', string='Proveedor')

    @api.model
    def create(self, vals):
        vals['clave'] = self.env['ir.sequence'].next_by_code('claveproducto')
        return super(Productos, self).create(vals)

    

    # @api.depends('valor_actual', 'depreciacion_anual', 'anos_vida_util', 'create_date')
    # def _compute_valor_depreciado(self):
    #     for producto in self:
    #         if producto.create_date:
    #             dias_transcurridos = (datetime.now() - producto.create_date).days
    #             depreciacion_diaria = producto.depreciacion_anual / 365.0 / 100.0 * producto.valor_actual
    #             depreciacion_acumulada = depreciacion_diaria * dias_transcurridos
    #             producto.valor_depreciado = producto.valor_actual - depreciacion_acumulada
    #         else:
    #             producto.valor_depreciado = producto.valor_actual
    @api.depends('valor_actual', 'depreciacion_anual', 'anos_vida_util')
    def _compute_valor_depreciado(self):
        for producto in self:
            if producto.create_date:
                # Convertir create_date a objeto datetime
                try:
                    create_date = datetime.strptime(producto.create_date, '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    create_date = datetime.strptime(producto.create_date, '%Y-%m-%d')

                dias_transcurridos = (datetime.now() - create_date).days

                if producto.anos_vida_util > 0:
                    depreciacion_diaria = (producto.depreciacion_anual / 100) * producto.valor_actual / 365
                    depreciacion_acumulada = depreciacion_diaria * dias_transcurridos
                    producto.valor_depreciado = producto.valor_actual - depreciacion_acumulada
                else:
                    producto.valor_depreciado = producto.valor_actual
            else:
                producto.valor_depreciado = producto.valor_actual


    @api.onchange('categoria')
    def _onchange_categoria(self):
        subcat_domain = []
        if self.categoria == 'inmuebles':
            subcat_domain = [('subcategoria', 'in', [
                'viviendas', 'edificios', 'infraestructura', 'otros_inmuebles'])]
        elif self.categoria == 'muebles':
            subcat_domain = [('subcategoria', 'in', [
                'muebles_oficina', 'muebles_excepcion', 'computo', 'otros_muebles', 'educacional', 
                'audiovisuales', 'deportivos', 'fotografia_video'])]
        elif self.categoria == 'medico':
            subcat_domain = [('subcategoria', 'in', [
                'equipo_medico', 'instrumental_medico'])]
        elif self.categoria == 'transporte':
            subcat_domain = [('subcategoria', 'in', [
                'automoviles', 'carrocerias', 'aeroespacial', 'ferroviario', 'embarcaciones', 'otros_transporte'])]
        elif self.categoria == 'maquinaria':
            subcat_domain = [('subcategoria', 'in', [
                'agropecuario', 'industrial', 'construccion', 'aire_acondicionado', 
                'telecomunicacion', 'electrico', 'herramientas', 'otros_equipos'])]
        elif self.categoria == 'biologicos':
            subcat_domain = [('subcategoria', 'in', [
                'bovinos', 'porcinos', 'aves', 'ovinos_caprinos', 'peces', 'equinos', 
                'zoologico', 'arboles_plantas', 'otros_biologicos'])]
        elif self.categoria == 'servicios':
            subcat_domain = [('subcategoria', 'in', [
                'mantenimiento_infraestructura', 'consultoria_academica', 'soporte_tecnico', 'capacitacion', 
                'limpieza', 'seguridad', 'administrativos'])]
        
        return {'domain': {'subcategoria': subcat_domain}}

    @api.onchange('subcategoria')
    def _onchange_subcategoria(self):
        # Valores predeterminados según la subcategoría seleccionada
        valores_por_defecto = {
            'viviendas': (50, 2),
            'edificios': (30, 3.3),
            'infraestructura': (25, 4),
            'otros_inmuebles': (20, 5),
            'muebles_oficina': (10, 10),
            'muebles_excepcion': (10, 10),
            'computo': (3, 33.3),
            'otros_muebles': (10, 10),
            'educacional': (10, 10),
            'audiovisuales': (3, 33.3),
            'deportivos': (5, 20),
            'fotografia_video': (3, 33.3),
            'equipo_medico': (5, 20),
            'instrumental_medico': (5, 20),
            'automoviles': (5, 20),
            'carrocerias': (5, 20),
            'aeroespacial': (5, 20),
            'ferroviario': (5, 20),
            'embarcaciones': (5, 20),
            'otros_transporte': (5, 20),
            'agropecuario': (10, 10),
            'industrial': (10, 10),
            'construccion': (10, 10),
            'aire_acondicionado': (10, 10),
            'telecomunicacion': (10, 10),
            'electrico': (10, 10),
            'herramientas': (10, 10),
            'otros_equipos': (10, 10),
            'bovinos': (5, 20),
            'porcinos': (5, 20),
            'aves': (5, 20),
            'ovinos_caprinos': (5, 20),
            'peces': (5, 20),
            'equinos': (5, 20),
            'zoologico': (5, 20),
            'arboles_plantas': (5, 20),
            'otros_biologicos': (5, 20),
            'mantenimiento_infraestructura': (5, 20),
            'consultoria_academica': (5, 20),
            'soporte_tecnico': (5, 20),
            'capacitacion': (5, 20),
            'limpieza': (5, 20),
            'seguridad': (5, 20),
            'administrativos': (5, 20),
        }
        if self.subcategoria in valores_por_defecto:
            vida_util, depreciacion_anual = valores_por_defecto[self.subcategoria]
            self.anos_vida_util = vida_util
            self.depreciacion_anual = depreciacion_anual

