from django.core.management.base import BaseCommand
from calculator.models import PlasticMaterial


class Command(BaseCommand):
    help = 'Load initial plastic material density data with common applications'

    def handle(self, *args, **kwargs):
        materials_data = [
            # ==================== PLASTIC FILMS ====================

            # LDPE Films
            {'name': 'LDPE', 'code': 'LDPE', 'material_type': 'FILM', 'density': 0.925,
             'description': 'Low-Density Polyethylene - Flexible, transparent, good moisture barrier',
             'common_uses': 'Carry bags, shrink wrap, agricultural films, packaging films, liners',
             'processing_temp_c': '160-180°C', 'tensile_strength_mpa': '8-20', 'elongation_percent': '300-600'},

            {'name': 'Colored LDPE', 'code': 'LDPE_colored', 'material_type': 'FILM', 'density': 0.925,
             'description': 'Colored LDPE with pigment additives',
             'common_uses': 'Colored carry bags, industrial packaging, identification films',
             'processing_temp_c': '160-180°C', 'tensile_strength_mpa': '8-18', 'elongation_percent': '300-500'},

            # HDPE Films
            {'name': 'HDPE', 'code': 'HDPE', 'material_type': 'FILM', 'density': 0.955,
             'description': 'High-Density Polyethylene - Stiff, strong, good chemical resistance',
             'common_uses': 'Shopping bags, grocery bags, trash bags, industrial liners, food packaging',
             'processing_temp_c': '180-220°C', 'tensile_strength_mpa': '20-35', 'elongation_percent': '100-1000'},

            {'name': 'Colored HDPE', 'code': 'HDPE_colored', 'material_type': 'FILM', 'density': 0.960,
             'description': 'Colored HDPE with enhanced opacity',
             'common_uses': 'Retail bags, institutional bags, colored liners, construction films',
             'processing_temp_c': '180-220°C', 'tensile_strength_mpa': '20-32', 'elongation_percent': '100-800'},

            # CPP Films
            {'name': 'CPP', 'code': 'CPP', 'material_type': 'FILM', 'density': 0.910,
             'description': 'Cast Polypropylene - Excellent clarity, good moisture barrier',
             'common_uses': 'Food packaging, textile packaging, stationery overwrap, laminations',
             'processing_temp_c': '200-240°C', 'tensile_strength_mpa': '25-40', 'elongation_percent': '300-600'},

            {'name': 'Metallized CPP', 'code': 'CPP_metallized', 'material_type': 'FILM', 'density': 0.910,
             'description': 'CPP with aluminum metallization for enhanced barrier properties',
             'common_uses': 'Snack foods packaging, confectionery, pharmaceutical packaging, barrier laminates',
             'processing_temp_c': '200-240°C', 'tensile_strength_mpa': '25-38', 'elongation_percent': '250-500'},

            {'name': 'Pearlized CPP', 'code': 'CPP_pearlized', 'material_type': 'FILM', 'density': 0.860,
             'description': 'CPP with pearlescent appearance, lower density due to cavitation',
             'common_uses': 'Premium packaging, cosmetic packaging, gift wraps, specialty bags',
             'processing_temp_c': '200-240°C', 'tensile_strength_mpa': '20-35', 'elongation_percent': '200-400'},

            # BOPP Films
            {'name': 'BOPP', 'code': 'BOPP', 'material_type': 'FILM', 'density': 0.905,
             'description': 'Biaxially Oriented Polypropylene - High clarity, excellent printability',
             'common_uses': 'Label films, transparent packaging, pressure-sensitive tapes, overwrap',
             'processing_temp_c': '220-260°C', 'tensile_strength_mpa': '120-200', 'elongation_percent': '80-150'},

            {'name': 'White/Colored BOPP', 'code': 'BOPP_white_colored', 'material_type': 'FILM', 'density': 0.905,
             'description': 'Pigmented BOPP for opaque or colored applications',
             'common_uses': 'Label substrates, prime labels, flexible packaging, printing substrates',
             'processing_temp_c': '220-260°C', 'tensile_strength_mpa': '100-180', 'elongation_percent': '70-130'},

            {'name': 'Metallized BOPP', 'code': 'BOPP_metallized', 'material_type': 'FILM', 'density': 0.905,
             'description': 'BOPP with vacuum metallized aluminum layer',
             'common_uses': 'Decorative packaging, barrier packaging, capacitor films, insulation',
             'processing_temp_c': '220-260°C', 'tensile_strength_mpa': '110-190', 'elongation_percent': '70-140'},

            {'name': 'Pearlized BOPP', 'code': 'BOPP_pearlized', 'material_type': 'FILM', 'density': 0.790,
             'description': 'Cavitated BOPP with pearlescent appearance and lower density',
             'common_uses': 'Premium labels, cosmetic packaging, luxury goods packaging, gift wraps',
             'processing_temp_c': '220-260°C', 'tensile_strength_mpa': '80-150', 'elongation_percent': '60-120'},

            {'name': 'Matt Finish BOPP', 'code': 'BOPP_matt', 'material_type': 'FILM', 'density': 0.855,
             'description': 'BOPP with matte surface for reduced gloss and enhanced printability',
             'common_uses': 'Book covers, premium labels, cosmetic packaging, high-end retail packaging',
             'processing_temp_c': '220-260°C', 'tensile_strength_mpa': '90-160', 'elongation_percent': '65-135'},

            # PET Films
            {'name': 'PET', 'code': 'PET', 'material_type': 'FILM', 'density': 1.365,
             'description': 'Polyethylene Terephthalate - High strength, excellent dimensional stability',
             'common_uses': 'Audio/video tapes, electrical insulation, release liners, industrial applications',
             'processing_temp_c': '260-300°C', 'tensile_strength_mpa': '150-300', 'elongation_percent': '70-130'},

            {'name': 'Twist PET', 'code': 'PET_twist', 'material_type': 'FILM', 'density': 1.335,
             'description': 'Special PET formulation for twist-wrap applications',
             'common_uses': 'Confectionery twist wrap, chocolate wrapping, candy packaging',
             'processing_temp_c': '250-290°C', 'tensile_strength_mpa': '120-250', 'elongation_percent': '80-150'},

            {'name': 'Metallized PET', 'code': 'PET_metallized', 'material_type': 'FILM', 'density': 1.365,
             'description': 'PET with aluminum metallization for high barrier properties',
             'common_uses': 'Flexible packaging laminates, insulation materials, decorative applications',
             'processing_temp_c': '260-300°C', 'tensile_strength_mpa': '140-280', 'elongation_percent': '65-120'},

            {'name': 'Twist Metallized PET', 'code': 'PET_twist_metallized', 'material_type': 'FILM', 'density': 1.335,
             'description': 'Metallized PET specifically for twist-wrap applications',
             'common_uses': 'Premium confectionery, chocolate bars, high-end candy packaging',
             'processing_temp_c': '250-290°C', 'tensile_strength_mpa': '110-230', 'elongation_percent': '75-140'},

            # Nylon Films
            {'name': 'NYLON', 'code': 'NYLON', 'material_type': 'FILM', 'density': 1.145,
             'description': 'Polyamide film - Excellent toughness, good gas barrier, high temperature resistance',
             'common_uses': 'Food packaging, medical packaging, industrial bags, vacuum packaging',
             'processing_temp_c': '220-260°C', 'tensile_strength_mpa': '70-150', 'elongation_percent': '250-400'},

            {'name': 'Colored NYLON', 'code': 'NYLON_colored', 'material_type': 'FILM', 'density': 1.145,
             'description': 'Pigmented nylon film for specialized applications',
             'common_uses': 'Industrial packaging, agricultural films, technical applications',
             'processing_temp_c': '220-260°C', 'tensile_strength_mpa': '65-140', 'elongation_percent': '200-350'},

            # General Polypropylene
            {'name': 'Polypropylene', 'code': 'PP', 'material_type': 'FILM', 'density': 0.908,
             'description': 'General purpose polypropylene film',
             'common_uses': 'General packaging, stationery, industrial wrapping, conversion applications',
             'processing_temp_c': '200-240°C', 'tensile_strength_mpa': '25-40', 'elongation_percent': '400-800'},

            # ==================== LAMINATION COMPONENTS ====================

            {'name': 'Ink', 'code': 'ink', 'material_type': 'INK', 'density': 1.100,
             'description': 'Printing ink for flexographic and gravure printing',
             'common_uses': 'Surface printing on plastic films, labels, packaging decoration',
             'viscosity_cps': '30-100', 'solvent_content': '60-80%'},

            {'name': 'Ethyl Acetate', 'code': 'ethyl_acetate', 'material_type': 'SOLVENT', 'density': 0.902,
             'description': 'Common solvent for ink dilution and adhesive systems',
             'common_uses': 'Ink solvent, adhesive dilution, cleaning agent in printing',
             'boiling_point_c': '77.1', 'flash_point_c': '-4'},

            {'name': 'Adhesive', 'code': 'adhesive', 'material_type': 'ADHESIVE', 'density': 1.050,
             'description': 'Lamination adhesive for bonding multiple film layers',
             'common_uses': 'Film-to-film lamination, foil lamination, multi-layer packaging',
             'solid_content': '30-50%', 'viscosity_cps': '200-800'},

            {'name': 'Hardener', 'code': 'hardener', 'material_type': 'HARDENER', 'density': 1.150,
             'description': 'Cross-linking agent for polyurethane adhesive systems',
             'common_uses': 'Adhesive curing, bond strength enhancement, heat resistance improvement',
             'mixing_ratio': '5-15%', 'pot_life_hours': '8-24'},
        ]

        created_count = 0
        updated_count = 0
        skipped_count = 0

        for data in materials_data:
            material, created = PlasticMaterial.objects.get_or_create(
                code=data['code'],
                defaults=data
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ Created: {material.name}'))
                created_count += 1
            else:
                # Update existing material with new information
                update_fields = ['name', 'material_type', 'density', 'description']
                needs_update = False

                for field in update_fields:
                    if getattr(material, field) != data[field]:
                        setattr(material, field, data[field])
                        needs_update = True

                # Add new fields if they exist in model
                for field in ['common_uses', 'processing_temp_c', 'tensile_strength_mpa', 'elongation_percent']:
                    if hasattr(material, field) and field in data:
                        if getattr(material, field) != data[field]:
                            setattr(material, field, data[field])
                            needs_update = True

                if needs_update:
                    material.save()
                    self.stdout.write(self.style.WARNING(f'🔄 Updated: {material.name}'))
                    updated_count += 1
                else:
                    self.stdout.write(self.style.NOTICE(f'⏭️  Already exists: {material.name}'))
                    skipped_count += 1

        # Summary
        self.stdout.write('\n' + '=' * 50)
        self.stdout.write(self.style.SUCCESS(f'📊 MATERIAL DATA LOAD SUMMARY:'))
        self.stdout.write(self.style.SUCCESS(f'✅ Created: {created_count} materials'))
        self.stdout.write(self.style.WARNING(f'🔄 Updated: {updated_count} materials'))
        self.stdout.write(self.style.NOTICE(f'⏭️  Skipped: {skipped_count} materials'))
        self.stdout.write(self.style.SUCCESS(f'📦 Total in database: {PlasticMaterial.objects.count()} materials'))
        self.stdout.write('=' * 50)
