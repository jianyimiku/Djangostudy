from tinymce.models import HTMLField
class Text(models.Model):
	str = HTMLField()

#在自定义视图中使用的时候
#模板中的需要写一个js
<script type="text/javascript">
	tinyMCE.init({
		'mode': 'textareas',
		'theme': 'advanced',
		'width': 800,
		'height': 600,
	})#将textarea标签变成富文本
</script>
