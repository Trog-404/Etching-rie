from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Menu,
    MenuItemHistogram,
    MenuItemTerms,
)

app_entry_point = AppEntryPoint(
    name='Remove class',
    description='New app entry point configuration for fabrication facilities.',
    app=App(
        label='Remove class',
        path='app',
        category='Fabrication facilities',
        description='App to search remove processes.',
        readme=' The findability reach the level of the single technique at disposal.',
        #        columns=Columns(
        #            selected=[''],
        #            options={
        #                'entry_id': Column(),
        #            },
        #        ),
        #    ),
#        menu=Menu(
#            size='sm',
#            items=[
#                MenuItemTerms(search_quantity='authors.name', options=5),
#                # This is a submenu whose items become visible once selected. It
#                # contains three items: one full-width histogram and two terms items
#                # which are displayed side-by-side.
#                Menu(
#                    title='Submenu',
#                    size='md',
#                    items=[
#                        MenuItemHistogram(search_quantity='upload_create_time'),
#                        # These items target data from a custom schema
#                        MenuItemTerms(
#                            width=6,
#                            search_quantity='data.quantity1#nomad_example.schema_packages.mypackage.MySchema',
#                        ),
#                        MenuItemTerms(
#                            width=6,
#                            search_quantity='data.quantity2#nomad_example.schema_packages.mypackage.MySchema',
#                        ),
#                    ],
#                ),
#            ],
#        ),
    ),
)
