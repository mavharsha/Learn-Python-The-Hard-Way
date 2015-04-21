formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing, which I loved,",
	"I called it my Little Precious Pig!",
	"She used to sing,",
	"I loved that."
)
