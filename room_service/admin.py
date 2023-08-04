from django.contrib import admin
from .models import RoomService, LangChoice

# 어드민 페이지 제목 컨트롤
admin.site.site_header = "Roomservice Admin"  # 어드민 페이지 상단의 텍스트
admin.site.site_title = "Roomservice Admin"   # 브라우저 탭의 제목
admin.site.index_title = "Roomservice Admin"  # 어드민 메인 페이지의 제목

class RoomServiceAdmin(admin.ModelAdmin):
    def PRD_name(self, obj):
        return obj.PRD_name

    def display_category(self, obj):
        return obj.category
    
    def description(self, obj):
        return obj.description

    def display_price(self, obj):
        return obj.price
    
    def display_content(self, obj):
        return obj.content    

    list_display = ('PRD_name','display_category','display_price','description',)  # 표시할 필드들
    list_filter = ('PRD_name',)  # 필터 옵션으로 사용할 필드들
    search_fields = ('PRD_name', 'description')  # 검색 기능을 사용할 필드들
    ordering = ('PRD_name',)  # 기본 정렬 순서
    readonly_fields = ('created_at', 'updated_at')  # 읽기 전용 필드

    PRD_name.short_description = '상품명'  # 필드 표시명 변경
    display_category.short_description = '카테고리'  # 필드 표시명 변경
    description.short_description = '설명'  # 필드 표시명 변경
    display_price.short_description = '가격'  # 필드 표시명 변경
    

admin.site.register(RoomService, RoomServiceAdmin)


class LangChoiceAdmin(admin.ModelAdmin):
    def lang(self, obj):
        return obj.lang
    def RoomNumber(self, obj):
        return obj.RoomNumber
    
admin.site.register(LangChoice, LangChoiceAdmin )


