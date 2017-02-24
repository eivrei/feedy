from pptx import Presentation


def extract(filepath):
    # Generates a list on the form [[title, point, point, ...], [title, point, point, ...], ...]
    prs = Presentation(filepath)
    all_data = []
    for slide in prs.slides:
        slide_data = []
        number_of_sub_questions = 0
        for shape in slide.shapes:
            sub_points = []
            last_level = 0
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                if paragraph.level > 1:
                    continue
                paragraph_text = "".join(run.text for run in paragraph.runs)
                # If point is subpoint -> make new question with subpoints as points
                if paragraph.level > last_level:
                    sub_points.extend([slide_data[-1], paragraph_text])
                    number_of_sub_questions += 1
                elif paragraph.level == 1:
                    sub_points.append(paragraph_text)
                elif paragraph.level < last_level:
                    all_data.append(sub_points)
                    slide_data.append(paragraph_text)
                    sub_points = []
                else:
                    slide_data.append(paragraph_text)
                last_level = paragraph.level
        all_data.insert(len(all_data) - number_of_sub_questions, slide_data)
    return all_data
# print(extract("/Users/eivindreime/git/pugruppe100/server/temp/test_1.pptx"))