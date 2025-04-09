from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from .serializer import ServerSerializer

server_list_docs = extend_schema(
    responses=ServerSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name='category',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description='Filter by server category name.',
            required=False
        ),
        OpenApiParameter(
            name='qty',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description='Limit the number of returned servers.',
            required=False
        ),
        OpenApiParameter(
            name='by_user',
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description='Return only servers where the current user is a member. Requires authentication.',
            required=False
        ),
        OpenApiParameter(
            name='by_server_id',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description='Return only the server with the given ID. Requires authentication.',
            required=False
        ),
        OpenApiParameter(
            name='with_num_members',
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description='Include the number of members for each server.',
            required=False
        ),
    ]
)
