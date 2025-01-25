from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from etching_rie.schema_packages.schema_package import m_package

        return m_package


schema_package_entry_point = NewSchemaPackageEntryPoint(
    name='NewSchemaPackage',
    description='New schema package entry point configuration.',
)

class EtchingEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from etching_rie.schema_packages.rie import m_package

        return m_package


sintering = EtchingEntryPoint(
    name='Etching',
    description='Schema package for describing a etching process.',
)
