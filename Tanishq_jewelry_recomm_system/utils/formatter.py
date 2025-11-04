# formatter.py

class ResultFormatter:
    """Formats recommendation results for display."""
    
    @staticmethod
    def format_html(recommendations):
        if not recommendations:
            print("No recommendations found.")  # Debug log
            return "No recommendations found."
    
        result_html = "<h3>Recommended Jewelry Items💍💎:</h3>"
        for i, rec in enumerate(recommendations, 1):
            metadata = rec["metadata"]
    
            # Start the recommendation tile
            result_html += f"<div style='margin-bottom:15px; padding:10px; border:1px solid #ddd; border-radius:5px;'>"
    
            # Add the title
            result_html += f"<h4>#{i}: {metadata.get('TITLE', 'unavailabe😔☹')}</h4>"
    
            # Add images side by side using Flexbox
            if metadata.get('LINK1') or metadata.get('LINK2'):
                result_html += "<div style='display: flex; gap: 10px; margin-bottom: 10px;'>"
                if metadata.get('LINK1'):
                    result_html += f"<img src='{metadata['LINK1']}' style='max-width: 300px; max-height: 300px; border-radius: 5px;'>"
                if metadata.get('LINK2'):
                    result_html += f"<img src='{metadata['LINK2']}' style='max-width: 300px; max-height: 300px; border-radius: 5px;'>"
                result_html += "</div>"
            else:
                result_html += "<p>No image available</p>"
    
            # Add metadata details
            result_html += f"<p><b>Tanishq design id:</b> {metadata.get('Design_ID', 'fetching...')}</p>"
            result_html += f"<p><b>Category:         </b> {metadata.get('CATEGORY_TYPE', 'fetching...')}</p>"
            result_html += f"<p><b>Carets:           </b> {metadata.get('GOLD_KARATAGE', 'fetching...')}</p>"
            result_html += f"<p><b>Description:      </b> {metadata.get('SHORT_DESCRIPTION', 'No description available')}</p>"
            result_html += f"<p><b>Price in 💲(approx):</b> $ {metadata.get('PRICE', 'N/A')}</p>"
            result_html += f"<p><b>Metal type:       </b> {metadata.get('METAL', 'fetching')}</p>"
            result_html += f"<p><b>Jewellery type:   </b> {metadata.get('JEWELLERY_TYPE', 'fetching...')}</p>"
            result_html += f"<p><b>Similarity👉👈Score:</b> {rec['similarity_score']:.4f}</p>"
    
            # Close the recommendation tile
            result_html += "</div>"
    
        print("HTML output generated:", result_html)  # Debug log
        return result_html



    
    @staticmethod
    def format_json(recommendations):
        """Format recommendations as JSON.
        
        Args:
            recommendations (list): List of recommendation dictionaries
            
        Returns:
            list: Clean JSON-serializable results
        """
        if not recommendations:
            return []
        
        results = []
        for rec in recommendations:
            results.append({
                "TITLE": rec["metadata"].get("TITLE", "Unknown"),
                "CATEGORY_TYPE": rec["metadata"].get("CATEGORY_TYPE", "Unknown"),
                "SHORT_DESCRIPTION": rec["metadata"].get("SHORT_DESCRIPTION", "No description"),
                "PRICE": rec["metadata"].get("PRICE", "N/A"),
                "similarity_score": round(rec["similarity_score"], 4),
                "image_link🔗": rec["metadata"].get("LINK1", None)
            })
        
        return results

















# # formatter.py

# class ResultFormatter:
#     """Formats recommendation results for display."""
    
#     @staticmethod
#     def format_html(recommendations):
#         if not recommendations:
#             print("No recommendations found.")  # Debug log
#             return "No recommendations found."
    
#         result_html = "<h3>Recommended Jewelry Items💍💎:</h3>"
#         for i, rec in enumerate(recommendations, 1):
#             metadata = rec["metadata"]

# # Key: 1, Value: {'filename': '36167805.jpg', 'Design_ID': '51O5PT2QN1BAP1_P', 'TITLE': nan, 'CATEGORY_TYPE': 'SET2', 
# #                 'PRICE': 406384.0, 'SHORT_DESCRIPTION': nan, 'METAL': 'Gold', 'JEWELLERY_TYPE': 'PLAIN', 'GOLD_KARATAGE': 18,
# #                 'METAL_COLOR': 'Yellow', 'LINK1': 'https://objectstorage.ap-hyderabad-1.oraclecloud.com/n/axpfa55nllwe/b/app-ea/o/ECOM_Manual_Enrichment/51O5PT2QN1BAP1.jpg',
# #                   'LINK2': nan, 'ID': '36167805'}


#             result_html += f"<div style='margin-bottom:15px; padding:10px; border:1px solid #ddd; border-radius:5px;'>"

#             result_html += f"<h4>#{i}: {metadata.get('TITLE', 'unavailabe😔☹')}</h4>"
            
#             if metadata.get('LINK1'):
#                 result_html += f"<p><img src='{metadata['LINK1']}' style='max-width:400px; max-height:400px;'></p>"
#                 result_html += f"<p><img src='{metadata['LINK2']}' style='max-width:400px; max-height:400px;'></p>"
                
#             else:
#                 result_html += "<p>No image available</p>"
                
#             result_html += f"<p><b>Tanishq design id:</b> {metadata.get('Design_ID', 'fetching...')}</p>"                        
#             result_html += f"<p><b>Category:         </b> {metadata.get('CATEGORY_TYPE', 'fetching...')}</p>"
#             result_html += f"<p><b>Carets:           </b> {metadata.get('GOLD_KARATAGE', 'fetching...')}</p>"
#             result_html += f"<p><b>Description:      </b> {metadata.get('SHORT_DESCRIPTION', 'No description available')}</p>"
#             result_html += f"<p><b>Price in 💲(approx):</b> $ {metadata.get('PRICE', 'N/A')}</p>"
#             result_html += f"<p><b>Metal type:       </b> {metadata.get('METAL', 'fetching')}</p>"
#             result_html += f"<p><b>Jewellery type:   </b> {metadata.get('JEWELLERY_TYPE', 'fetching...')}</p>"
#             # result_html += f"<p><b>Ornament color: </b> {metadata.get('METAL_COLOR', 'fetching...')}</p>"
#             result_html += f"<p><b>Similarity👉👈Score:</b> {rec['similarity_score']:.4f}</p>"
#             # result_html += f"<p><b>img link🔗:</b> {metadata.get('LINK1','No link found')} </p>"
             
           
#             result_html += "</div>"
    
#         print("HTML output generated:", result_html)  # Debug log
#         return result_html    
#     @staticmethod
#     def format_json(recommendations):
#         """Format recommendations as JSON.
        
#         Args:
#             recommendations (list): List of recommendation dictionaries
            
#         Returns:
#             list: Clean JSON-serializable results
#         """
#         if not recommendations:
#             return []
        
#         results = []
#         for rec in recommendations:
#             results.append({
#                 "TITLE": rec["metadata"].get("TITLE", "Unknown"),
#                 "CATEGORY_TYPE": rec["metadata"].get("CATEGORY_TYPE", "Unknown"),
#                 "SHORT_DESCRIPTION": rec["metadata"].get("SHORT_DESCRIPTION", "No description"),
#                 "PRICE": rec["metadata"].get("PRICE", "N/A"),
#                 "similarity_score": round(rec["similarity_score"], 4),
#                 "image_link🔗": rec["metadata"].get("LINK1", None)
#             })
        
#         return results

