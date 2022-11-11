# HIPAA-834-file-processor
Script for processing EDI834 file types into parseable benefit rosters for verification of coverage

This is not a plug-and-play solution, as the 834 EDI file type spec is an extremly old ANSI-based spec and has been implemented differently by nearly every benefit-providing organization.

See: https://en.wikipedia.org/wiki/ANSI_834_Enrollment_Implementation_Format
for some information on it.

Also: https://edination.com/edi-formats.html for a vivid illustration of how fragmented this "standard" is.

That said, if you can reverse engineer via context or have some internal documentation as to how the sectors implemented within your organization, this might be a passable framework for building a parser.
