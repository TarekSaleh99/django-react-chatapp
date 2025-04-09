from rest_framework import viewsets
from .models import Server
from .serializer import ServerSerializer
from rest_framework.response import Response
from .schema import server_list_docs
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from django.db.models import Count

class ServerListViewSet(viewsets.ViewSet): # ask GPT about this later

    queryset = Server.objects.all()
    
    @server_list_docs
    def list(self, request):
        category = request.query_params.get('category')
        qty = request.query_params.get('qty')
        by_user = request.query_params.get('by_user') == 'true'
        by_server_id = request.query_params.get('by_server_id')
        with_num_members = request.query_params.get('with_num_members') == 'true'

        if (by_user or by_server_id) and not request.user.is_authenticated:
            raise AuthenticationFailed()

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        if by_user:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)
        
        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=Count('member'))

        if by_server_id:
            try:
                self.queryset = self.queryset.filter(id=by_server_id)
                if not self.queryset.exists():
                    raise ValidationError(detail=f"Server with id {by_server_id} not found")
            except ValueError:
                raise ValidationError(detail="Server value error")
        if qty:
            self.queryset = self.queryset[: int(qty)]
        
       
        
        serializer = ServerSerializer(self.queryset, many=True, context={'num_members':with_num_members})
        return Response(serializer.data)
    



